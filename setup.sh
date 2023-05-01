#!/bin/bash

if command -v python3 >/dev/null 2>&1
then
else
  echo "Python 3 is not installed!"
  exit 1
fi

echo "Do you want to start the setup. Make sure the file.py is in the same directory as the setup and you have installed Python3.10 or higher"
read -p "Enter Y or N: " choice

if [[ "$choice" == "N" ]]; then
    exit 1
else
    if [[ -f "file.py" ]]; then
        if [[ -d "/usr/lib/python3.10/" ]]; then
            cp file.py "/usr/lib/python3.10/"
            echo "Finish setup"
            read -p "Press any key to continue..." key
            exit 0
        elif [[ -d "/usr/lib/python3.11/" ]]; then
            cp file.py "/usr/lib/python3.11/"
            echo "Finish setup"
            read -p "Press any key to continue..." key
            exit 0
        else
            echo "If it don't work maybe your Python libs are not saved at /usr/lib/python3.11/ or /usr/lib/python3.10/"
            echo "You can do manual the setup by copy the file.py to your python libs. Normally they are at /lib/python3.11/ or /lib/python3.10/"
            read -p "Press any key to continue..." key
            exit 1
        fi
    else
        echo "Can't start setup. Make sure the file.py is in the same directory as the setup"
        read -p "Press any key to continue..." key
        exit 1
    fi
fi
