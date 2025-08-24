# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowQhvlmY.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(337, 407)
        MainWindow.setStyleSheet(u"background-color:black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 301, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.edit_query = QLineEdit(self.centralwidget)
        self.edit_query.setObjectName(u"edit_query")
        self.edit_query.setGeometry(QRect(30, 90, 251, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 71, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 141, 16))
        self.label_3.setFont(font1)
        self.spin_display = QSpinBox(self.centralwidget)
        self.spin_display.setObjectName(u"spin_display")
        self.spin_display.setMinimum(10)
        self.spin_display.setGeometry(QRect(30, 160, 61, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 220, 111, 16))
        self.label_6.setFont(font1)
        self.btn_search = QPushButton(self.centralwidget)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setGeometry(QRect(110, 290, 131, 31))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	background-color:navy;\n"
"	color:white;\n"
"	border-radius:6px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:black;\n"
"}")
        self.combo_sort = QComboBox(self.centralwidget)
        self.combo_sort.addItem("")
        self.combo_sort.addItem("")
        self.combo_sort.setObjectName(u"combo_sort")
        self.combo_sort.setGeometry(QRect(30, 240, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 337, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84 \ub274\uc2a4 \uac80\uc0c9\uae30", None))
        self.edit_query.setText("")
        self.edit_query.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9 \uacb0\uacfc \uac1c\uc218(\ucd5c\uc18c 10)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9 \uae30\uc900", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.combo_sort.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc815\ud655\ub3c4\uc21c", None))
        self.combo_sort.setItemText(1, QCoreApplication.translate("MainWindow", u"\ub0a0\uc9dc\uc21c", None))

    # retranslateUi

