# -----------------------------------------------------------------------------
# Project: P-File repair
#
# What: A simple tool to repair certain GE p-files that are corrupted. This is specifically a problem for certain 
# v. 28 p-files. These files always contains 10058420 bytes and contains a lot of unused 0 values. The following 
# software removes these values and creates a new file.
# 
# Currently, the software only works with v. 28 files. If you encounter this problem with other files and wish to 
# use this software, please submit a feature request.
# 
# Some code is adapted from the "spant" package (https://cran.r-project.org/web/packages/spant/index.html).
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from modules.user_interface import MainWindow

# ------------------------------------------------------------- #
# 2 - Application start                                         #
# ------------------------------------------------------------- #
if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)

    # Change style
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon(':/Logo/icon.icon'))

    # Show GUI window
    window = MainWindow()
    window.show()

    # App execute/loop
    sys.exit(app.exec_())