#!/bin/sh
echo Copying data from temp to data.
cp /openweb-ui-temp-data/webui.db /openweb-ui-data/webui.db
cp /gpt-sovits-temp-data/GPT_weights/xiaote.ckpt /GPT_weights/xiaote.ckpt
cp /gpt-sovits-temp-data/GPT_weights/xiaote.pth /GPT_weights/xiaote.pth
cp /gpt-sovits-temp-data/SoVITS_weights/xiaote.pth /SoVITS_weights/xiaote.pth
cp /gpt-sovits-temp-data/wavs/xiaote.wav /wavs/xiaote.wav
exec "$@"