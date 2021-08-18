:: Load packages
pip install -r requirements.txt  # Requirments

:: Build UI
pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py
pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

:: Create requirements
pip freeze > requirements.txt

:: Build file (pyinstaller)
pyinstaller --specpath "pyinstaller" ^
    --workpath "pyinstaller\build" ^
    --distpath "pyinstaller\dist" ^
    --onefile ^
    --noconfirm ^
    --noconsole ^
    --icon=..\resources\graphics\icon.ico ^
    repair_p_file.py