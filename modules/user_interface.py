# -----------------------------------------------------------------------------
# Module: User interface
#
# What:User interface logic and definitions.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize

# Local functions 

# Local classes 
from modules.classes import PFile

# Local resources 


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class MainWindow(QMainWindow):
    '''Contains all functions and interactions with main user interace.

    Args:
        None
    
    Returns:
        None
    
    '''

    # [Class attributes] #

    # [Instance attributes] #
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize user self
        self.initialize_ui()

        # Custom widgets
        self.custom_widgets()

        # Settings/prefrences
        self.load_settings()

        # Connections
        self.connections()

    # [Functions] #
    def initialize_ui(self):
        ''' [Class function] - Loads UI '''
        
        # Load UI from imported py/ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window title
        self.setWindowTitle("P-file repair")

        # Set window size
        window_size = QSize(1350, 800) # [TODO] - Make smaller
        self.resize(window_size)
        self.setMinimumSize(window_size)