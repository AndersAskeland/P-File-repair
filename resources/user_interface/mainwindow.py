# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1110, 485)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_top = QFrame(self.centralwidget)
        self.sidebar_top.setObjectName(u"sidebar_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_top.sizePolicy().hasHeightForWidth())
        self.sidebar_top.setSizePolicy(sizePolicy)
        self.sidebar_top.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar_top.setAutoFillBackground(False)
        self.sidebar_top.setFrameShape(QFrame.NoFrame)
        self.sidebar_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.sidebar_top)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 60, -1)
        self.img_logo = QLabel(self.sidebar_top)
        self.img_logo.setObjectName(u"img_logo")
        self.img_logo.setMinimumSize(QSize(80, 80))
        self.img_logo.setMaximumSize(QSize(80, 80))
        self.img_logo.setPixmap(QPixmap(u":/Logo/logo.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setWordWrap(False)

        self.horizontalLayout.addWidget(self.img_logo)

        self.label_title = QLabel(self.sidebar_top)
        self.label_title.setObjectName(u"label_title")
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMaximumSize(QSize(16777215, 16777215))
        self.label_title.setTextFormat(Qt.RichText)
        self.label_title.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_title)


        self.verticalLayout_2.addWidget(self.sidebar_top)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.frame_concent = QFrame(self.content)
        self.frame_concent.setObjectName(u"frame_concent")
        self.frame_concent.setFrameShape(QFrame.NoFrame)
        self.frame_concent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_concent)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 12, -1, 0)
        self.description_1 = QLabel(self.frame_concent)
        self.description_1.setObjectName(u"description_1")

        self.verticalLayout_3.addWidget(self.description_1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.description_3 = QLabel(self.frame_concent)
        self.description_3.setObjectName(u"description_3")

        self.verticalLayout_3.addWidget(self.description_3)

        self.frame_folder_selection = QFrame(self.frame_concent)
        self.frame_folder_selection.setObjectName(u"frame_folder_selection")
        self.frame_folder_selection.setMinimumSize(QSize(0, 0))
        self.frame_folder_selection.setFrameShape(QFrame.NoFrame)
        self.frame_folder_selection.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_folder_selection)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_selection = QLineEdit(self.frame_folder_selection)
        self.lineEdit_selection.setObjectName(u"lineEdit_selection")
        self.lineEdit_selection.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_selection)

        self.btn_select_folder = QPushButton(self.frame_folder_selection)
        self.btn_select_folder.setObjectName(u"btn_select_folder")

        self.horizontalLayout_5.addWidget(self.btn_select_folder)

        self.btn_select_file = QPushButton(self.frame_folder_selection)
        self.btn_select_file.setObjectName(u"btn_select_file")

        self.horizontalLayout_5.addWidget(self.btn_select_file)


        self.verticalLayout_3.addWidget(self.frame_folder_selection)


        self.horizontalLayout_3.addWidget(self.frame_concent)


        self.verticalLayout_2.addWidget(self.content)

        self.sidebar_bottom = QFrame(self.centralwidget)
        self.sidebar_bottom.setObjectName(u"sidebar_bottom")
        self.sidebar_bottom.setMinimumSize(QSize(0, 0))
        self.sidebar_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.sidebar_bottom.setFrameShape(QFrame.NoFrame)
        self.sidebar_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_bottom)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 12)
        self.horizontalSpacer = QSpacerItem(530, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_convert = QDialogButtonBox(self.sidebar_bottom)
        self.btn_convert.setObjectName(u"btn_convert")
        sizePolicy.setHeightForWidth(self.btn_convert.sizePolicy().hasHeightForWidth())
        self.btn_convert.setSizePolicy(sizePolicy)
        self.btn_convert.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.btn_convert)


        self.verticalLayout_2.addWidget(self.sidebar_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1110, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">P-file repair</span></p><p align=\"justify\"><span style=\" font-size:18pt;\">Tool to repair corrupted GE p-files.</span></p></body></html>", None))
        self.description_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Select P-file</span></p><p>Select a single p-file or a entire folder that contain p-files that you wish to repair.</p></body></html>", None))
        self.description_3.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.lineEdit_selection.setPlaceholderText("")
        self.btn_select_folder.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.btn_select_file.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
    # retranslateUi

