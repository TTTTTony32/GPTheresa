#!/bin/sh
cp /openweb-ui-temp-data/webui.db /openweb-ui-data/webui.db
cp -R /gpt-sovits-temp-data/GPT_weights /gpt-sovits-cpu-data/
cp -R /gpt-sovits-temp-data/SoVITS_weights /gpt-sovits-gpu-data/
cp -R /gpt-sovits-temp-data/wavs /gpt-sovits-cpu-data/
exec "$@"