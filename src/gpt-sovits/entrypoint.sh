#!/bin/sh
cd /gpt-sovits-data
cat gpt-sovits.tar.* | tar -zxvf -
exec "$@"