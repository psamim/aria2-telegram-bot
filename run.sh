#!/usr/bin/env bash

set -e

export TOKEN="TOKEN"
VENV_NAME="venv"
VENV=$PWD/$VENV_NAME

# Setup virtualenv
virtualenv $VENV_NAME
source $VENV/bin/activate

# Install requirements
pip install -r requirements.txt

# Start diana and the bot
./diana/dad start
./bot.py
./diana/dad stop
