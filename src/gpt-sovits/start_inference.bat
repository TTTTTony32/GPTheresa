@echo off
chcp 65001
set gpt_path=GPT_weights/xiaote.ckpt
set sovits_path=SoVITS_weights/xiaote.pth
set cnhubert_path=GPT_SoVITS/pretrained_models/chinese-hubert-base
set bert_path=GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large
runtime\python GPT_SoVITS/inference_webui.py all_zh