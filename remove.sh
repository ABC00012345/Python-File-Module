#!/bin/bash

read -p "Do you really want to remove it? [Y/N] " user_input

if [ "$user_input" == "N" ]; then
    exit
else
    rm /usr/lib/python3.10/file.py
    rm /usr/lib/python3.11/file.py
fi

if [ -f /usr/lib/python3.10/file.py -o -f /usr/lib/python3.11/file.py ]; then
    echo "Failed! Please remove it yourself: /usr/lib/python3.11/ or /usr/lib/python3.10/"
else
    echo "Successfully removed!"
fi
