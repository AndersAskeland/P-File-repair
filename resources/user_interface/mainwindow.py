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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1110, 545)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_top = QFrame(self.centralwidget)
        self.sidebar_top.setObjectName(u"sidebar_top")
        self.sidebar_top.setMaximumSize(QSize(16777215, 120))
        self.sidebar_top.setAutoFillBackground(False)
        self.sidebar_top.setFrameShape(QFrame.NoFrame)
        self.sidebar_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.sidebar_top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img_logo = QLabel(self.sidebar_top)
        self.img_logo.setObjectName(u"img_logo")

        self.horizontalLayout.addWidget(self.img_logo)

        self.label_title = QLabel(self.sidebar_top)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setTextFormat(Qt.RichText)

        self.horizontalLayout.addWidget(self.label_title)


        self.verticalLayout_2.addWidget(self.sidebar_top)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_concent = QFrame(self.content)
        self.frame_concent.setObjectName(u"frame_concent")
        self.frame_concent.setFrameShape(QFrame.NoFrame)
        self.frame_concent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_concent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(12, -1, -1, 0)
        self.description_1 = QLabel(self.frame_concent)
        self.description_1.setObjectName(u"description_1")

        self.verticalLayout_3.addWidget(self.description_1)

        self.description_2 = QLabel(self.frame_concent)
        self.description_2.setObjectName(u"description_2")

        self.verticalLayout_3.addWidget(self.description_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.description_3 = QLabel(self.frame_concent)
        self.description_3.setObjectName(u"description_3")

        self.verticalLayout_3.addWidget(self.description_3)

        self.frame_folder_selection = QFrame(self.frame_concent)
        self.frame_folder_selection.setObjectName(u"frame_folder_selection")
        self.frame_folder_selection.setMinimumSize(QSize(0, 50))
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

        self.frame_header = QFrame(self.content)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(300, 0))
        self.frame_header.setMaximumSize(QSize(300, 16777215))
        self.frame_header.setFrameShape(QFrame.NoFrame)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_header)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_header)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.stackedWidget = QStackedWidget(self.frame_header)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_header)


        self.verticalLayout_2.addWidget(self.content)

        self.sidebar_bottom = QFrame(self.centralwidget)
        self.sidebar_bottom.setObjectName(u"sidebar_bottom")
        self.sidebar_bottom.setMaximumSize(QSize(16777215, 40))
        self.sidebar_bottom.setFrameShape(QFrame.NoFrame)
        self.sidebar_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_bottom)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(848, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.sidebar_bottom)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_4.addWidget(self.btn_cancel)

        self.btn_convert = QPushButton(self.sidebar_bottom)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setMinimumSize(QSize(150, 0))
        self.btn_convert.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.btn_convert)


        self.verticalLayout_2.addWidget(self.sidebar_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1110, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.btn_convert.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_logo.setText(QCoreApplication.translate("MainWindow", u"    LOGO    ", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt;\">P-file repair</span></p><p><span style=\" font-family:'Menlo','Monaco','Courier New','monospace'; font-size:14pt; color:#d4d4d4;\">A simple tool to repair certain GE p-files that are corrupted. This <br/>is specifically a problem for certain v. 28 p-files.</span></p></body></html>", None))
        self.description_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Select P-file</span></p></body></html>", None))
        self.description_2.setText(QCoreApplication.translate("MainWindow", u"Select  singular file or a folder containing P-files that you wish to repair.", None))
        self.description_3.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.lineEdit_selection.setPlaceholderText("")
        self.btn_select_folder.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.btn_select_file.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

