# -----------------------------------------------------------------------------
# Module: User interface
#
# What: User interface logic and definitions.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import QSize

# Local functions 

# Local classes 
from modules.classes import pFile

# Local resources 
from resources.user_interface.mainwindow import Ui_MainWindow


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    '''Main user interface window.
    
    Class that contains all functions and interactions related to
    the main user interace, including initialization of ui, loading
    custom widgets and settings and establishing ui connections.

    Inherits UI file from resources/user_interface/mainwindow.ui.

    Args:
        None
    
    Attributes:
        None
    '''

    # ---- Constructor ---- #
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        # General variables
        self.p_file_path = None
        self.folder = False

        # Define user interface
        self.setupUi(self)
        self.setWindowTitle("P-file repair")

        window_size = QSize(1350/1.4, 800/2) # TODO: Remember to change size
        self.resize(window_size)
        self.setMinimumSize(window_size)
        
        # Signals
        self.btn_select_folder.clicked.connect(self.select_p_folder)
        self.btn_select_file.clicked.connect(self.select_p_file)
        self.btn_convert.clicked.connect(self.convert_p_file)


    # ---- Slots ---- #
    def select_p_folder(self) -> None:
        ''' Select folder containing several p-files. '''
        self.dialog_file_dialog(folder=True)
        
    def select_p_file(self,) -> None:
        ''' Select single file p-file. '''
        self.dialog_file_dialog(folder=False)

    def convert_p_file(self) -> None:
        ''' Converts p_file or folder of p-files. '''
        self.convert_p_file()


    # ---- Functions ---- #
    def dialog_file_dialog(self, folder: bool) -> None:
        ''' Dialog to select folder or file using native wizard. 
        
        Args:
            None
    
        Attributes:
            None
        '''
        print(folder)
        dlg = QFileDialog()
        
        # Check if folder or file.
        if self.folder:
            dlg.setLabelText(QFileDialog.Accept, "Select directory")
            dlg.setFileMode(QFileDialog.Directory)
            dlg.Option.ShowDirsOnly
            self.folder = True 
        else:
            dlg.setLabelText(QFileDialog.Accept, "Select p-file")
            dlg.setFileMode(QFileDialog.ExistingFile)
            dlg.setNameFilter("P-files (*.7)")
            self.folder = False

        # Retrieve selection
        if dlg.exec_():
            self.p_file_path = dlg.selectedFiles()[0]
            self.lineEdit_selection.setText(str(self.p_file_path))

    def convert_p_file(self) -> None:
        ''' Converts the selected P-file or files using the pFile class.

        Args:
            None
    
        Attributes:
            None        
        '''

        # Check if folder or single file
        if self.folder:
            pass #TODO: Go trough dict and find *.7 files. Make loop thereafter. Remember to do error checking (if no pfile).
        else:
            # Define class
            p_file = pFile(path=self.p_file_path, folder=self.folder)

            # Write TODO: define output surfix
            p_file.write_data(path="/Users/andersaskeland/Documents/Statistics (Local)/GE_MRI/test_GUI.7")