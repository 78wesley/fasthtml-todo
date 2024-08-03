#!/bin/sh

# Create venv and install requirements if not exist
if [ ! -e '.venv/' ]; then
    python3.12 -m venv .venv
    .venv/bin/pip install -r requirements.txt
fi

# Start flask server
.venv/bin/python3 main.py