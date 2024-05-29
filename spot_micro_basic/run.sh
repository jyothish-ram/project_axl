#!/bin/bash

pidfile="$HOME/spotmicroai/.lock"
if [ -f "$pidfile" ] && kill -0 "$(cat "$pidfile")" 2>/dev/null; then
    echo still running
    exit 1
fi
echo $$ > $pidfile

cd ~/spotmicroai || exit

export PYTHONPATH=.

venv/bin/python3 spotmicroai/main.py
