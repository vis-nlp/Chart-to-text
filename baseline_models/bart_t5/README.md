# Chart-to-text with T5/BART



The repo is adapted from [Transformers-summarization](https://github.com/huggingface/transformers/tree/main/examples/pytorch/summarization).


## Setup

Follow [this link](https://github.com/huggingface/transformers/tree/main/examples/pytorch/summarization) to setup the dependecency and dataset preprocess (to custom JSONLINES files). Note that we concatenate the chart title and the chart together by seperating them with "\<s\>".




## Training T5/BART for Chart-to-Text

#### Training command for T5:

```bash
 CUDA_VISIBLE_DEVICES=0,1 python examples/pytorch/summarization/run_summarization.py     \
 --model_name_or_path t5-base   \
 --do_train --do_eval     \
 --train_file YOURDATA/train.json \
 --validation_file YOURDATA/validation.json \
 --test_file YOURDATA/test.json     \
 --source_prefix "translate Chart to Text: "     \
 --output_dir YOUR_SAVE_PATH   --overwrite_output_dir     \
 --max_target_length 256 \
 --per_device_train_batch_size=2     \
 --per_device_eval_batch_size=4 \
 --text_column text    \
 --summary_column summary \
 --evaluation_strategy steps \
 --eval_accumulation_steps 1000 \
 --save_steps 2000 \
 --eval_steps 2000 \
 --num_train_epochs 200 \
 --fp16
```



#### Training command for BART:

```bash
 CUDA_VISIBLE_DEVICES=0,1 python examples/pytorch/summarization/run_summarization.py     \
 --model_name_or_path facebook/bart-base   \
 --do_train --do_eval     \
 --train_file YOURDATA/train.json \
 --validation_file YOURDATA/validation.json \
 --test_file YOURDATA/test.json     \
 --output_dir YOUR_SAVE_PATH   --overwrite_output_dir     \
 --max_target_length 256 \
 --per_device_train_batch_size=2     \
 --per_device_eval_batch_size=4 \
 --text_column text    \
 --summary_column summary \
 --evaluation_strategy steps \
 --eval_accumulation_steps 1000 \
 --save_steps 2000 \
 --eval_steps 2000 \
 --num_train_epochs 200 \
 --fp16
```





#### Evaluation

The following code is for evaluating BART. Add ` --source_prefix   "translate Table to Text: "  ` to the following command when evaluating T5.

```
 CUDA_VISIBLE_DEVICES=0 python examples/pytorch/summarization/run_summarization.py    \
 --model_name_or_path YOUR_BEST_CHECKPOINT   \
 --do_predict    \
 --train_file YOURDATA/train.json \
 --validation_file YOURDATA/validation.json \
 --test_file YOURDATA/test.json     \
 --output_dir YOUR_OUTPUT_FILE     --overwrite_output_dir     \
 --per_device_eval_batch_size=20 \
 --text_column text    \
 --summary_column summary \
 --predict_with_generate \
```

Generated text is in `YOUR_OUTPUT_FILE`. You can then use any metrics to evaluate.

