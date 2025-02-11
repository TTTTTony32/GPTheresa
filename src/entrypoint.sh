#!/bin/sh
cd /gpt-sovits
cat gpt-sovits.tar.* | tar -xvf - -C /gpt-sovits
exec "$@"