# Go to direct location
cd "~/GitHub/P-File-repair"

# Activate virtual enviorment
source ~/.pyenv/versions/repair_p_file/bin/activate

# Build UI file using uic
pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py

# Create icons
pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

# Run file
python repair_p_file.py