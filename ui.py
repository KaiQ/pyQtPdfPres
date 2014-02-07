# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './GUI/pyQtPdfPres.ui'
#
# Created: Fri Feb  7 01:49:54 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Episoder(object):
    def setupUi(self, Episoder):
        Episoder.setObjectName(_fromUtf8("Episoder"))
        Episoder.resize(473, 325)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Episoder.sizePolicy().hasHeightForWidth())
        Episoder.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtGui.QHBoxLayout(Episoder)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.prev = QtGui.QLabel(Episoder)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev.sizePolicy().hasHeightForWidth())
        self.prev.setSizePolicy(sizePolicy)
        self.prev.setMinimumSize(QtCore.QSize(100, 100))
        self.prev.setObjectName(_fromUtf8("prev"))
        self.verticalLayout.addWidget(self.prev)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.active = QtGui.QLabel(Episoder)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.active.sizePolicy().hasHeightForWidth())
        self.active.setSizePolicy(sizePolicy)
        self.active.setAlignment(QtCore.Qt.AlignCenter)
        self.active.setObjectName(_fromUtf8("active"))
        self.verticalLayout_2.addWidget(self.active)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.next = QtGui.QLabel(Episoder)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy)
        self.next.setMinimumSize(QtCore.QSize(100, 100))
        self.next.setObjectName(_fromUtf8("next"))
        self.verticalLayout_3.addWidget(self.next)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.lcdNumber = QtGui.QLCDNumber(Episoder)
        self.lcdNumber.setNumDigits(4)
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 1337)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.verticalLayout_3.addWidget(self.lcdNumber)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Stop = QtGui.QPushButton(Episoder)
        self.Stop.setObjectName(_fromUtf8("Stop"))
        self.horizontalLayout_2.addWidget(self.Stop)
        self.bStart = QtGui.QPushButton(Episoder)
        self.bStart.setObjectName(_fromUtf8("bStart"))
        self.horizontalLayout_2.addWidget(self.bStart)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Episoder)
        QtCore.QMetaObject.connectSlotsByName(Episoder)

    def retranslateUi(self, Episoder):
        Episoder.setWindowTitle(_translate("Episoder", "Episoder", None))
        self.prev.setText(_translate("Episoder", "TextLabel", None))
        self.active.setText(_translate("Episoder", "TextLabel", None))
        self.next.setText(_translate("Episoder", "TextLabel", None))
        self.Stop.setText(_translate("Episoder", "Stop", None))
        self.bStart.setText(_translate("Episoder", "Start", None))

