# -----------------------------------------------------------------------------
# MODULE: Custom widgets and properties   
#
# WHAT: Custom widgets and property classifications   
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
import random
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFrame, QLabel, QGraphicsDropShadowEffect, QPushButton, QTabWidget
from PySide2.QtGui import QColor

# Local functions 

# Local classes 

# Local resources 


# ------------------------------------------------------------------------------
# 2 - Settings & constants
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# 3 - Widgets
# ------------------------------------------------------------------------------
# Card widget
class QCard(QFrame):
    '''Qt widget for cards
    
    Custom Qt widget for cards. Attempts to recreate the google material theme card system. 

    TODO:
        * Shadows are not perfect

    Args:
        None

    Attributes:
        shadow (QtObject): Shadow effect.
    '''

    # ---- Class attributes ---- #
    def __init__(self,parent=None):
        super().__init__(parent)
        
        # Drop shadow effect. TODO: Make it like google material design.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setColor(QColor (0,0,0,200)) 
        self.shadow.setBlurRadius(6)
        self.shadow.setOffset(0, 3)
        self.setGraphicsEffect(self.shadow)

        # Color
        self.setStyleSheet("background-color: #2a313d; border-radius: 10px")

# Slidding widget
class SlidingStackedWidget(QtWidgets.QStackedWidget):
    '''Qt widget for sliding stacked widget
    
    Custom Qt widget for a sliding stacked widget.

    TODO:
        * Actually implement

    Args:
        None

    Attributes:
        ****
    '''

    # ---- Class attributes ---- #
    def __init__(self, parent=None):
        super(SlidingStackedWidget, self).__init__(parent)

        self.m_direction = QtCore.Qt.Horizontal
        self.m_speed = 500
        self.m_animationtype = QtCore.QEasingCurve.OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QtCore.QPoint(0, 0)
        self.m_active = False



class QDatabaseSettings(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        # Drop shadow effect. TODO: Make it like google material design.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setColor(QColor (0,0,0,200)) 
        self.shadow.setBlurRadius(6)
        self.shadow.setOffset(0, 3)
        self.setGraphicsEffect(self.shadow)


# ------------------------------------------------------------------------------
# 4 - Properties
# ------------------------------------------------------------------------------
class QSideBar(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

class QTextTitle(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)

class QSmallButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        
class QMenuButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

class QMediumButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

class QTextOutput(QLabel):
    def __init__(self,parent=None):
        super().__init__(parent)

