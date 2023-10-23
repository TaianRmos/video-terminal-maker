@echo off
rem Try pip
pip install -r requirements.txt

rem Check if pip was successful
if errorlevel 1 (
    rem If pip wasn't successful, try pip3
    echo "pip failed, trying pip3"
    pause
    pip3 install -r requirements.txt

    if errorlevel 1 (
        echo "pip installation failed, please verify your pip installation"
        pause
        exit
    )
)

rem Try to find the right version of python then launch the script
python --version
if errorlevel 1 (
    python3 --version
    if errorlevel 1 (
        echo "'python' and 'python3' failed, please verify your python installation"
        pause
        exit
    )
    python3 scripts/project_maker.py
    pause
)
python scripts/project_maker.py
pause