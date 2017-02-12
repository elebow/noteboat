#!/bin/sh

. virtualenv/bin/activate

export FLASK_DEBUG=1
export FLASK_APP=noteboat.py

export NOTEBOAT_BASE_DIR=$PWD

cd noteboat
flask run --host=0.0.0.0
