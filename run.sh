#!/usr/bin/env bash

export TOKEN="TOKEN"
VENV=$PWD/venv
source $VENV/bin/activate
pip install -r requirements.txt
./diana/dad start
./bot.py
./diana/dad stop
