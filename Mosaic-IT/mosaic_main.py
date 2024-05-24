import json
import random
import argparse
from tqdm import tqdm

import numpy as np
from transformers import AutoTokenizer

from mosaic_formats_rules import *


def get_random_indicators(args):

    if args.version == 'format':
        # 0
        overall_indicator = 0
    elif args.version == 'order':
        # 0, 1
        overall_indicator = random.randint(0, 1)
    elif args.version == 'mask':
        # 0, 2
        overall_indicator = random.randint(0, 1)
        overall_indicator = 2 if overall_indicator == 1 else overall_indicator
    elif args.version == 'both':
        # 0, 1, 2
        overall_indicator = random.randint(0, 2)
    # 0 for format only, 1 for format + order, 2 for format + mask

    ################################################
    # FORMAT VERSION
    ################################################

    digit_tag_idx = random.randint(0, len(DIGITS_TAG_LIST)-1)
    digit_punc_idx = random.randint(0, len(DIGITS_PUNC_LIST)-1)
    begin_end_tag_punc_idx = random.randint(0, len(BEGIN_END_TAG_PUNC_LIST)-1)
    begin_end_text_idx = random.randint(0, len(BEGIN_END_TEXT_LIST)-1)
    format_instruction_interval_tag_idx = random.randint(0, len(FORMAT_INSTRUCTION_INTERVAL_TAG_LIST)-1)
    fomat_meta_instruction_idx = random.randint(0, len(FORMAT_META_INSTRUCTION_LIST)-1)
    fomat_meta_instruction_no_idx = random.randint(0, len(FORMAT_META_INSTRUCTION_NO_LIST)-1)
    format_overall_instruction_idx = random.randint(0, len(FORMAT_OVERALL_INSTRUCTION_LIST)-1)

    newline_for_digit = random.choice([True, False])
    lowercase_for_begin_end_text = random.choice([True, False])
    do_begin_end_format = random.choice([True, False])
    do_no_begin_end_format_no_ins = random.choice([True, False])

    ################################################
    # ORDER VERSION
    ################################################

    order_method_idx = random.randint(0, len(ORDER_METHOD_INSTRUCTION_PAIR_DICT)-1)
    order_method = list(ORDER_METHOD_INSTRUCTION_PAIR_DICT.keys())[order_method_idx]
    order_meta_instruction_idx = random.randint(0, len(ORDER_METHOD_INSTRUCTION_PAIR_DICT[order_method])-1)
    order_overall_instruction_idx = random.randint(0, len(ORDER_OVERALL_INSTRUCTION_LIST)-1)
    order_seq_tag_idx = random.randint(0, len(ORDER_SEQ_TAG_LIST)-1)
    order_seq_interval_idx = random.randint(0, len(ORDER_SEQ_INTERVAL_LIST)-1)

    order_fixed_list = [i for i in range(MAX_INSTRUCTION_NUMBER)]
    random.shuffle(order_fixed_list)

    ################################################
    # MASk VERSION
    ################################################

    mask_method_idx = random.randint(0, len(MASK_METHOD_INSTRUCTION_PAIR_DICT)-1)
    mask_method = list(MASK_METHOD_INSTRUCTION_PAIR_DICT.keys())[mask_method_idx]
    mask_meta_instruction_idx = random.randint(0, len(MASK_METHOD_INSTRUCTION_PAIR_DICT[mask_method])-1)
    mask_overall_instruction_idx = random.randint(0, len(MASK_OVERALL_INSTRUCTION_LIST)-1)
    mask_seq_tag_idx = random.randint(0, len(MASK_SEQ_TAG_LIST)-1)
    mask_seq_interval_idx = random.randint(0, len(MASK_SEQ_INTERVAL_LIST)-1)

    mask_ratio = random.uniform(MASK_RATIO_RANGE[0], MASK_RATIO_RANGE[1])
    mask_fixed_list = [i for i in range(MAX_INSTRUCTION_NUMBER)]
    random.shuffle(mask_fixed_list)


    # Wrap all indicators
    random_indicators = {
        'overall_indicator':overall_indicator,
        # Format version
        'digit_tag_idx':digit_tag_idx,
        'digit_punc_idx':digit_punc_idx,
        'begin_end_tag_punc_idx':begin_end_tag_punc_idx,
        'begin_end_text_idx':begin_end_text_idx,
        'format_instruction_interval_tag_idx':format_instruction_interval_tag_idx,
        'fomat_meta_instruction_idx':fomat_meta_instruction_idx,
        'fomat_meta_instruction_no_idx':fomat_meta_instruction_no_idx,
        'format_overall_instruction_idx':format_overall_instruction_idx,
        'newline_for_digit':newline_for_digit,
        'lowercase_for_begin_end_text':lowercase_for_begin_end_text,
        'do_begin_end_format':do_begin_end_format,
        'do_no_begin_end_format_no_ins':do_no_begin_end_format_no_ins,

        # Order version
        'order_method_idx':order_method_idx,
        'order_meta_instruction_idx':order_meta_instruction_idx,
        'order_overall_instruction_idx':order_overall_instruction_idx, 
        'order_fixed_list':order_fixed_list,
        'order_seq_tag_idx':order_seq_tag_idx,
        'order_seq_interval_idx':order_seq_interval_idx,

        # Mask version
        'mask_method_idx':mask_method_idx,
        'mask_meta_instruction_idx':mask_meta_instruction_idx,
        'mask_overall_instruction_idx':mask_overall_instruction_idx,
        'mask_ratio':mask_ratio,
        'mask_fixed_list':mask_fixed_list,
        'mask_seq_tag_idx':mask_seq_tag_idx,
        'mask_seq_interval_idx':mask_seq_interval_idx,
    }

    return random_indicators

# Format only
def get_formated_data(random_indicators, used_items_temp):

    # Build instruction format
    if random_indicators['digit_tag_idx'] == 0:
        instruction_digit = ''
    else:
        instruction_digit = DIGITS_TAG_LIST[random_indicators['digit_tag_idx']] + DIGITS_PUNC_LIST[random_indicators['digit_punc_idx']]
        instruction_digit = instruction_digit + '\n' if random_indicators['newline_for_digit'] else instruction_digit
    
    # Build response format
    if random_indicators['do_begin_end_format']:

        # Get begin and end tag for instructions and responses
        begin_text, end_text = BEGIN_END_TEXT_LIST[random_indicators['begin_end_text_idx']][0], BEGIN_END_TEXT_LIST[random_indicators['begin_end_text_idx']][1]
        begin_text = begin_text.lower() if random_indicators['lowercase_for_begin_end_text'] else begin_text
        end_text = end_text.lower() if random_indicators['lowercase_for_begin_end_text'] else end_text

        begin_tag = BEGIN_END_TAG_PUNC_LIST[random_indicators['begin_end_tag_punc_idx']].format(text=begin_text)
        end_tag = BEGIN_END_TAG_PUNC_LIST[random_indicators['begin_end_tag_punc_idx']].format(text=end_text)

        # Get meta instruction
        meta_instruction = FORMAT_META_INSTRUCTION_LIST[random_indicators['fomat_meta_instruction_idx']]
        meta_instruction = meta_instruction.format(begin_tag=begin_tag, end_tag=end_tag)

        pass
    else:
        begin_tag, end_tag = '', ''

        # Get meta instruction
        if random_indicators['do_no_begin_end_format_no_ins']:
            meta_instruction = ''
        else:
            meta_instruction = FORMAT_META_INSTRUCTION_NO_LIST[random_indicators['fomat_meta_instruction_no_idx']]

    # Get overall instruction
    overall_instruction = FORMAT_OVERALL_INSTRUCTION_LIST[random_indicators['format_overall_instruction_idx']]

    instruction_all = ''
    response_all = ''
    # Process real data
    for i, data_i in enumerate(used_items_temp):
        instruction_i = data_i['instruction'] + '\n' + data_i['input'] if data_i['input'] != '' else data_i['instruction']
        response_i = data_i['output']

        # Get formated instruction_i
        instruction_digit_i = instruction_digit.format(i=i+1)
        instruction_i = instruction_digit_i + instruction_i

        # Get formated response_i
        response_i = instruction_digit_i + begin_tag + response_i + end_tag

        instruction_all += instruction_i
        response_all += response_i

        if i != len(used_items_temp) - 1:
            instruction_all += FORMAT_INSTRUCTION_INTERVAL_TAG_LIST[random_indicators['format_instruction_interval_tag_idx']]
            response_all += '\n\n\n'

        pass

    # Get real overall instruction
    overall_instruction = overall_instruction.format(meta_instruction=meta_instruction,instruction_all=instruction_all)

    return {'instruction':overall_instruction, 'output':response_all}

def get_ordered_response_list(random_indicators, instruction_list_ori, response_list_formated):

    order_method = list(ORDER_METHOD_INSTRUCTION_PAIR_DICT.keys())[random_indicators['order_method_idx']]

    if order_method == 'FIX':
        # Use the fix order
        order_fixed_list = random_indicators['order_fixed_list']
        # Remove the numbers greater than the length of the instruction list
        order_fixed_list = [i for i in order_fixed_list if i < len(instruction_list_ori)]
        ordered_response_list = [response_list_formated[i] for i in order_fixed_list]
    elif order_method == 'REVERSE':
        # Reverse the order
        ordered_response_list = response_list_formated[::-1]
    elif order_method == 'ALPHA':
        # Sort according to the first letter of each instruction
        ordered_response_list = [response for _, response in sorted(zip(instruction_list_ori, response_list_formated), key=lambda pair: pair[0])]
    elif order_method == 'REVERSE_ALPHA':
        # Sort according to the first letter of each instruction, reverse
        ordered_response_list = [response for _, response in sorted(zip(instruction_list_ori, response_list_formated), key=lambda pair: pair[0], reverse=True)]
    elif order_method == 'LENGTH_WORD':
        # Sort according to the word length of each instruction
        ordered_response_list = [response for _, response in sorted(zip(instruction_list_ori, response_list_formated), key=lambda pair: len(pair[0].split()))]
    elif order_method == 'REVERSE_LENGTH_WORD':
        # Sort according to the word length of each instruction, reverse
        ordered_response_list = [response for _, response in sorted(zip(instruction_list_ori, response_list_formated), key=lambda pair: len(pair[0].split()), reverse=True)]
    elif order_method == 'LENGTH_CHAR':
        # Sort according to the character length of each instruction
        ordered_response_list = [response for _, response in sorted(zip(instruction_list_ori, response_list_formated), key=lambda pair: len(pair[0]))]
    elif order_method == 'REVERSE_LENGTH_CHAR':
        # Sort according to the character length of each instruction, reverse
        ordered_response_list = [response for _, response in sorted(zip(instruction_list_ori, response_list_formated), key=lambda pair: len(pair[0]), reverse=True)]
    elif order_method == 'ODD_EVEN':
        # First respond to the odd-numbered instructions, then the even-numbered ones, Note: i startes from 0
        ordered_response_list = []
        for i, response in enumerate(response_list_formated):
            if i % 2 == 0:
                ordered_response_list.append(response)
        for i, response in enumerate(response_list_formated):
            if i % 2 != 0:
                ordered_response_list.append(response)
    elif order_method == 'EVEN_ODD':
        # First respond to the even-numbered instructions, then the odd-numbered ones, Note: i startes from 0
        ordered_response_list = []
        for i, response in enumerate(response_list_formated):
            if i % 2 != 0:
                ordered_response_list.append(response)
        for i, response in enumerate(response_list_formated):
            if i % 2 == 0:
                ordered_response_list.append(response)
    
    return ordered_response_list

def get_masked_response_list(random_indicators, instruction_list_ori, response_list_formated):

    mask_method = list(MASK_METHOD_INSTRUCTION_PAIR_DICT.keys())[random_indicators['mask_method_idx']]

    if mask_method == 'FIX':
        # Ignore the instructions in the fixed list
        mask_threshold = max(int(len(instruction_list_ori) * random_indicators['mask_ratio']),1)
        mask_fixed_list = random_indicators['mask_fixed_list']
        mask_fixed_list = [i for i in mask_fixed_list if i < len(instruction_list_ori)]
        masked_response_list = [response for i, response in enumerate(response_list_formated) if i not in mask_fixed_list[:mask_threshold]]
    elif mask_method == 'WORD_LONG':
        # Ignore the longest n instructions
        instruction_length_list = [len(instruction.split()) for instruction in instruction_list_ori]
        sorted_pairs = sorted(enumerate(instruction_length_list), key=lambda x: x[1], reverse=True)
        sorted_indices = [index for index, value in sorted_pairs]
        mask_threshold = max(int(len(instruction_list_ori) * random_indicators['mask_ratio']),1)
        mask_fixed_list = sorted_indices[:mask_threshold]
        masked_response_list = [response for i, response in enumerate(response_list_formated) if i not in mask_fixed_list[:mask_threshold]]
    elif mask_method == 'WORD_SHORT':
        # Ignore the shortest n instructions
        instruction_length_list = [len(instruction.split()) for instruction in instruction_list_ori]
        sorted_pairs = sorted(enumerate(instruction_length_list), key=lambda x: x[1], reverse=False)
        sorted_indices = [index for index, value in sorted_pairs]
        mask_threshold = max(int(len(instruction_list_ori) * random_indicators['mask_ratio']),1)
        mask_fixed_list = sorted_indices[:mask_threshold]
        masked_response_list = [response for i, response in enumerate(response_list_formated) if i not in mask_fixed_list[:mask_threshold]]
    elif mask_method == 'ODD':
        # Ignore the odd-numbered instructions, keep the even, Note: i startes from 0
        masked_response_list = [response for i, response in enumerate(response_list_formated) if i % 2 != 0]
    elif mask_method == 'EVEN':
        # Ignore the odd-numbered instructions, keep the odd, Note: i startes from 0
        masked_response_list = [response for i, response in enumerate(response_list_formated) if i % 2 == 0]

    return masked_response_list

def wrap_instruction_response(random_indicators, instruction_list_formated, response_list_formated):
    instruction_all = ''
    response_all = ''
    for i, instruction_i in enumerate(instruction_list_formated):
        instruction_all += instruction_i
        if i != len(instruction_list_formated) - 1:
            instruction_all += FORMAT_INSTRUCTION_INTERVAL_TAG_LIST[random_indicators['format_instruction_interval_tag_idx']]
    
    for i, response_i in enumerate(response_list_formated):
        response_all += response_i
        if i != len(response_list_formated) - 1:
            response_all += '\n\n'

    return instruction_all, response_all

# Format + order + mask
def get_formated_data_pro(random_indicators, used_items_temp):

    # Build instruction format
    if random_indicators['digit_tag_idx'] == 0:
        instruction_digit = ''
    else:
        instruction_digit = DIGITS_TAG_LIST[random_indicators['digit_tag_idx']] + DIGITS_PUNC_LIST[random_indicators['digit_punc_idx']]
        instruction_digit = instruction_digit + '\n' if random_indicators['newline_for_digit'] else instruction_digit
    
    # Build response format
    if random_indicators['do_begin_end_format']:

        # Get begin and end tag for instructions and responses
        begin_text, end_text = BEGIN_END_TEXT_LIST[random_indicators['begin_end_text_idx']][0], BEGIN_END_TEXT_LIST[random_indicators['begin_end_text_idx']][1]
        begin_text = begin_text.lower() if random_indicators['lowercase_for_begin_end_text'] else begin_text
        end_text = end_text.lower() if random_indicators['lowercase_for_begin_end_text'] else end_text

        begin_tag = BEGIN_END_TAG_PUNC_LIST[random_indicators['begin_end_tag_punc_idx']].format(text=begin_text)
        end_tag = BEGIN_END_TAG_PUNC_LIST[random_indicators['begin_end_tag_punc_idx']].format(text=end_text)

        # Get meta instruction
        meta_instruction = FORMAT_META_INSTRUCTION_LIST[random_indicators['fomat_meta_instruction_idx']]
        meta_instruction = meta_instruction.format(begin_tag=begin_tag, end_tag=end_tag)

        pass
    else:
        begin_tag, end_tag = '', ''

        # Get meta instruction
        if random_indicators['do_no_begin_end_format_no_ins']:
            meta_instruction = ''
        else:
            meta_instruction = FORMAT_META_INSTRUCTION_NO_LIST[random_indicators['fomat_meta_instruction_no_idx']]

    # Get overall instruction
    format_overall_instruction_format = FORMAT_OVERALL_INSTRUCTION_LIST[random_indicators['format_overall_instruction_idx']]

    instruction_list_ori = []
    instruction_list_formated = []
    response_list_formated = []
    for i, data_i in enumerate(used_items_temp):
        instruction_i = data_i['instruction'] + '\n' + data_i['input'] if data_i['input'] != '' else data_i['instruction']
        response_i = data_i['output']

        # Get formated instruction_i
        instruction_digit_i = instruction_digit.format(i=i+1)
        instruction_i_formated = instruction_digit_i + instruction_i

        # Get formated response_i
        response_i_formated = instruction_digit_i + begin_tag + response_i + end_tag

        instruction_list_ori.append(instruction_i)
        instruction_list_formated.append(instruction_i_formated)
        response_list_formated.append(response_i_formated)

    if random_indicators['overall_indicator'] == 0 or len(instruction_list_ori) == 1:
        # Format only
        # If there is only one instruction, we do not need to do the order or mask
        instruction_all, response_all = wrap_instruction_response(random_indicators, instruction_list_formated, response_list_formated)
        overall_instruction = format_overall_instruction_format.format(meta_instruction=meta_instruction,instruction_all=instruction_all)
    
    elif random_indicators['overall_indicator'] == 1:
        # Format + order
        order_method = list(ORDER_METHOD_INSTRUCTION_PAIR_DICT.keys())[random_indicators['order_method_idx']]
        ordered_response_list = get_ordered_response_list(random_indicators, instruction_list_ori, response_list_formated)
        assert len(ordered_response_list) == len(response_list_formated)
        instruction_all, response_all = wrap_instruction_response(random_indicators, instruction_list_formated, ordered_response_list)

        order_meta_instruction = ORDER_METHOD_INSTRUCTION_PAIR_DICT[order_method][random_indicators['order_meta_instruction_idx']]
        order_overall_instruction_format = ORDER_OVERALL_INSTRUCTION_LIST[random_indicators['order_overall_instruction_idx']]

        if order_method == 'FIX':
            order_fixed_list = random_indicators['order_fixed_list']
            order_fixed_list = [i for i in order_fixed_list if i < len(instruction_list_ori)]
            seq = ''
            for idx_list, idx_real in enumerate(order_fixed_list):
                if idx_list != len(order_fixed_list) - 1:
                    seq = seq + str(idx_real+1) + ORDER_SEQ_INTERVAL_LIST[random_indicators['order_seq_interval_idx']]
                else:
                    seq = seq + str(idx_real+1)
            seq = ORDER_SEQ_TAG_LIST[random_indicators['order_seq_tag_idx']].format(i=seq)
            order_meta_instruction = order_meta_instruction.format(seq)
            pass

        instruction_all = format_overall_instruction_format.format(meta_instruction=meta_instruction,instruction_all=instruction_all)
        overall_instruction = order_overall_instruction_format.format(meta_instruction=order_meta_instruction,instruction_all=instruction_all)

    elif random_indicators['overall_indicator'] == 2:
        # Format + mask
        mask_method = list(MASK_METHOD_INSTRUCTION_PAIR_DICT.keys())[random_indicators['mask_method_idx']]
        masked_response_list = get_masked_response_list(random_indicators, instruction_list_ori, response_list_formated)
        instruction_all, response_all = wrap_instruction_response(random_indicators, instruction_list_formated, masked_response_list)

        mask_meta_instruction = MASK_METHOD_INSTRUCTION_PAIR_DICT[mask_method][random_indicators['mask_meta_instruction_idx']]
        mask_overall_instruction_format = MASK_OVERALL_INSTRUCTION_LIST[random_indicators['mask_overall_instruction_idx']]

        if mask_method == 'FIX':
            mask_threshold = max(int(len(instruction_list_ori) * random_indicators['mask_ratio']),1)
            mask_fixed_list = random_indicators['mask_fixed_list']
            mask_fixed_list = [i for i in mask_fixed_list if i < len(instruction_list_ori)]
            mask_fixed_list = mask_fixed_list[:mask_threshold]
            seq = ''
            for idx_list, idx_real in enumerate(mask_fixed_list):
                if idx_list != len(mask_fixed_list) - 1:
                    seq = seq + str(idx_real+1) + MASK_SEQ_INTERVAL_LIST[random_indicators['mask_seq_interval_idx']]
                else:
                    seq = seq + str(idx_real+1)
            seq = MASK_SEQ_TAG_LIST[random_indicators['mask_seq_tag_idx']].format(i=seq)
            mask_meta_instruction = mask_meta_instruction.format(seq)
            pass
        elif mask_method in ['WORD_LONG', 'WORD_SHORT']:
            mask_threshold = max(int(len(instruction_list_ori) * random_indicators['mask_ratio']),1)
            mask_meta_instruction = mask_meta_instruction.format(mask_threshold)
            pass

        instruction_all = format_overall_instruction_format.format(meta_instruction=meta_instruction,instruction_all=instruction_all)
        overall_instruction = mask_overall_instruction_format.format(meta_instruction=mask_meta_instruction,instruction_all=instruction_all)

    return {'instruction':overall_instruction, 'output':response_all}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default='data/alpaca_gpt4_data.json')
    parser.add_argument("--save_path", type=str, default='xxx.json')
    parser.add_argument("--model_name_or_path", type=str, default='meta-llama/Llama-2-7b-hf')
    parser.add_argument("--max_length", type=int, default=2000)
    parser.add_argument("--epo_num", type=int, default=4)
    parser.add_argument("--wrap_mode", type=str, default='uniform', 
        choices=['uniform', 'max_length', 'fix_max', 'exp', 'pareto', 'lognormal', 'logistic2'])
    parser.add_argument("--wrap_max_num", type=int, default=10)
    parser.add_argument("--version", type=str, default='both', choices=['format', 'order', 'mask', 'both'])
    args = parser.parse_args()
    return args


def main():

    args = parse_args()
    print(args)

    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)

    def get_token_count(text):
        # Tokenize the text and return the number of tokens
        # input_ids = tokenizer.encode(text, return_tensors="pt")
        return len(tokenizer.tokenize(text))

    # Load the original data from the file
    with open(args.data_path, 'r') as file:
        original_data = json.load(file)

    all_shuffled_data = []  # Master list to hold all shuffled data

    for epo in tqdm(range(args.epo_num)):
        shuffled_data = original_data.copy()  # Create a copy of the original data for each shuffle
        random.shuffle(shuffled_data)

        i = 0
        while i < len(shuffled_data):
            if args.wrap_mode == 'uniform':
                chunk_size = random.randint(1, args.wrap_max_num)
            elif args.wrap_mode == 'fix_max':
                chunk_size = args.wrap_max_num
            elif args.wrap_mode == 'max_length':  
                chunk_size = len(shuffled_data) - i
            elif args.wrap_mode == 'exp':
                while True:
                    random_num = np.random.exponential()
                    if random_num < args.wrap_max_num:
                        break
                chunk_size = args.wrap_max_num - int(random_num)
            elif args.wrap_mode == 'pareto':
                while True:
                    random_num = np.random.pareto(1)-1
                    if random_num < args.wrap_max_num:
                        break
                chunk_size = args.wrap_max_num - int(random_num)
            elif args.wrap_mode == 'lognormal':
                while True:
                    random_num = np.random.lognormal()
                    if random_num < args.wrap_max_num:
                        break
                chunk_size = args.wrap_max_num - int(random_num)
            elif args.wrap_mode == 'logistic2':
                while True:
                    random_num = np.random.logistic(scale=2.0)
                    if random_num < args.wrap_max_num and random_num > 0:
                        break
                chunk_size = args.wrap_max_num - int(random_num)

            end_i = i+chunk_size if i+chunk_size < len(shuffled_data) else len(shuffled_data)
            selected_items = shuffled_data[i:end_i]

            count = 0
            used_items_temp = []
            formated_data_real = {}
            for j, item in enumerate(selected_items):
                if 'input' not in item.keys():
                    item['input'] = ''
                used_items_temp.append(item)
                random_indicators = get_random_indicators(args)
                formated_data_temp = get_formated_data_pro(random_indicators, used_items_temp)

                if get_token_count(formated_data_temp['instruction'] + formated_data_temp['output']) < args.max_length:
                    count += 1
                    formated_data_real = {
                                    "instruction": formated_data_temp['instruction'],
                                    "output": formated_data_temp['output'],
                                    "count": count,
                                    }
                else:
                    break  # Stop adding items to this chunk if token limit is exceeded

            if formated_data_real != {}:
                all_shuffled_data.append(formated_data_real)
                i += count  # Move to the next chunk starting position
            else:
                i += 1

    # Store all concatenated groups in a new JSON file
    with open(args.save_path, 'w') as outfile:
        json.dump(all_shuffled_data, outfile, indent=4)


if __name__ == "__main__":
    main()
