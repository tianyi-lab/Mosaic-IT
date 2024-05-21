# Mosaic-IT

This is the repo for the Mosaic-IT project, which introduces an augmentation method for Instruction Tuning. 

## Install

Install the dependencies with `pip install -r requirements.txt`

Note: The use of Mosaic-IT only needs the ```transformers``` package, thus if you are using a different code base with ```transformers``` installed, you can directly run the code and manually install the missing packages.

## Run Code

```
python Mosaic-IT/mosaic_main.py \
    --data_path data/alpaca_gpt4_data.json \
    --save_path alpaca_gpt4_data_mosaicked.json \
    --model_name_or_path meta-llama/Llama-2-7b-hf \
    --epo_num 4 \
    --wrap_mode uniform \
    --wrap_max_num 10 \
    --version both
```

```--data_path```: Input data, in alpaca format. <br>
```--save_path```: Save data path. <br>
```--model_name_or_path```: The model used to calculate the token counts. <br>
```--epo_num```: The times of random mosaic process to be run. <br>
```--wrap_mode```: How to decide the distribution of the number of instructions. <br>
```--wrap_max_num```: Max number of instructions. <br>
```--version```: Mosaic Strateties. <br>

## Training

We use the prompt and code base from [FastChat](https://github.com/lm-sys/FastChat):

```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: Hi ASSISTANT: Hello.</s>USER: Who are you? ASSISTANT: I am ...</s>......
```
