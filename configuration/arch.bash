#!/bin/bash

sudo pacman -Syu

sudo pacman -S python python-pip npm

pip install pipenv
sudo npm install -g sass