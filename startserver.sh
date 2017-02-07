#!/bin/sh

. virtualenv/bin/activate

export FLASK_DEBUG=1
export FLASK_APP=noteboat.py

cd noteboat
flask run --host=0.0.0.0
