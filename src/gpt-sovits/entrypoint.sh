#!/bin/sh
cat /gpt-sovits-data/gpt-sovits.tar.* | tar -zxvf - -C /gpt-sovits-data/
exec "$@"