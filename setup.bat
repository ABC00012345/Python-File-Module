@echo off
cls

@echo off
where python > nul 2>&1
if %errorlevel% == 0 (
) else (
    echo Python is not installed!
    exit
)

echo Do you want to start the setup. Make sure the file.py is in the same directory as the setup
choice /c YN

if errorlevel 2 (
    exit
) else (

    if exist file.py (

        if exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib" (
            copy file.py "C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib"
            echo Finish setup
            pause
            exit
        ) else (
            echo If it don't work maybe your Python libs are not saved at C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib
            echo You can do manaual the setup by copy the file.py to your python libs. Normally they are at C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\Lib
            pause
            exit
        )

    ) else (
        echo Can't start setup. Make sure the file.py is in the same directory as the setup
        pause
        exit
    )

)
