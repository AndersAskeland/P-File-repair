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
import glob
import re
import os
from pathlib import Path # Window specific paths
from PySide2.QtWidgets import QDialogButtonBox, QMainWindow, QFileDialog, QMessageBox, QWizard, QWizardPage
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
        self.btn_convert.button(QDialogButtonBox.Ok).setText("Convert")
        self.btn_convert.button(QDialogButtonBox.Ok).setEnabled(False)

        window_size = QSize(1350/1.4, 800/2)
        self.resize(window_size)
        self.setFixedSize(window_size)
        
        # Signals
        self.btn_select_folder.clicked.connect(self.select_p_folder)
        self.btn_select_file.clicked.connect(self.select_p_file)
        self.btn_convert.accepted.connect(self.convert_p_file)
        self.btn_convert.rejected.connect(self.exit_program)


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

    def exit_program(self) -> None:
        ''' Exits probram. '''
        self.close()


    # ---- Functions ---- #
    def convert_p_file(self) -> None:
        ''' Converts the selected P-file or files using the pFile class.

        Args:
            None
    
        Attributes:
            None        
        '''

        # Check if folder or single file
        if self.folder:
            glob_path = Path(self.p_file_path)  # Ensures compatable path over UNIX and Windows
            os.chdir(glob_path)

            # Check if there are actual p-files in folder
            if not glob.glob("*.7"):
                self.message_box(type=QMessageBox.Warning, message="No P-files found.")
                return 0
            
            # Read all files
            for p_file_path in glob_path.glob("*.7"):
                output_path = os.path.splitext(p_file_path)[0] + "_repaired.7"

                # Fix p-file
                p_file = pFile(path=p_file_path, folder=self.folder)
                p_file.repair_p_file(output_path)

            # Information message    
            self.message_box(type=QMessageBox.Information, message="P-files were successfully repaired.")
            return 0

        else:
            output_path = os.path.splitext(self.p_file_path)[0] + "_repaired.7"

            # Fix p-file
            p_file = pFile(path=self.p_file_path, folder=self.folder)
            if p_file.check_bad_data() == False:
                self.message_box(type=QMessageBox.Warning, message="Sum of bad data is not equal to 0. Possible deletion of real data occured.")
                return 0
    
            p_file.repair_p_file(output_path)

            # Message
            self.message_box(type=QMessageBox.Information, message="P-file was successfully repaired.")


    # ---- Dialogs ---- #
    def dialog_file_dialog(self, folder: bool) -> None:
        ''' Dialog to select folder or file using native wizard. '''

        dlg = QFileDialog()
        
        # Check if folder or file.
        if folder:
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
            self.btn_convert.button(QDialogButtonBox.Ok).setEnabled(True)
    
    def message_box(self, type: QMessageBox, message: str) -> None:
        ''' Dialog that display warnings '''
        dlg = QMessageBox(self)
        
        dlg.setWindowTitle(message)
        dlg.setText(message)
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.setIcon(type)
        
        dlg.exec_()