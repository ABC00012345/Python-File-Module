
@echo off
cls

echo Do you really want to remove the it?
choice /c YN

if errorlevel 2 (
    exit
) else (
    del C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib\file.py
)

if not exist C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib\file.py (
    echo Successfully removed!
) else (
    echo Failed! Plese remove it yourself: C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib\file.py
)