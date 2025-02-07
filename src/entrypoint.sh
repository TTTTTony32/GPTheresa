#!/bin/sh
echo Copying data from temp to data.
cp -R /openweb-ui-temp-data/* /openweb-ui-data/
cp -R /gpt-sovits-temp-data/GPT_weights/* /GPT_weights/
cp -R /gpt-sovits-temp-data/SoVITS_weights/* /SoVITS_weights/
cp -R /gpt-sovits-temp-data/wavs/* /wavs/
exec "$@"