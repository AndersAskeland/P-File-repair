# Go to direct location
cd "~/GitHub/P-File-repair"

# Activate virtual enviorment
source ~/.pyenv/versions/repair_p_file/bin/activate

# Build UI file using uic
pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py

# Create icons
pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

# Create requirements
pip freeze > requirements.txt

# Build file
pyinstaller --specpath "pyinstaller" \
    --workpath "pyinstaller/build" \
    --distpath "pyinstaller/dist" \
    --log-level=WARN \
    --add-data="../resources/graphics:resources/graphics" \
    --windowed \
    --noconfirm \
    --icon=icon.ico \
    repair_p_file.py