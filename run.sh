#!/usr/bin/env bash

export TOKEN="TOKEN"
VENV=$PWD/venv
source $VENV/bin/activate
./diana/dad start
./bot.py
./diana/dad stop
