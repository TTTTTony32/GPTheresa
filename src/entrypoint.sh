#!/bin/sh
cd /gpt-sovits
cat gpt-sovits.tar.* | tar -zxvf -
exec "$@"