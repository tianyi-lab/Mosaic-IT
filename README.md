# Mosaic-IT

This is the repo for the Mosaic-IT project, which introduces an augmentation method for Instruction Tuning. 

## News

- [2024/01] We released the Mosaic-IT code.

## Overview

TBD

## Highlights

TBD

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

```--data_path```: Input data, in alpaca format. 
```--save_path```: Save data path.
```--model_name_or_path```: The model used to calculate the token counts. 
```--epo_num```: The times of random mosaic process to be run. 
```--wrap_mode```: How to decide the distribution of the number of instructions.
```--wrap_max_num```: Max number of instructions. 
``--version```: Mosaic Strateties. 

## ToDo
- [ ] Release the code and papers. 
