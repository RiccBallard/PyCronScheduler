# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rballard/work/workspace/ProjectDirector/src/UIs/PDIRMainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_PDRMainWindow(object):
    def setupUi(self, PDRMainWindow):
        PDRMainWindow.setObjectName(_fromUtf8("PDRMainWindow"))
        PDRMainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PDRMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        PDRMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PDRMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PDRMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PDRMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PDRMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PDRMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PDRMainWindow)

    def retranslateUi(self, PDRMainWindow):
        PDRMainWindow.setWindowTitle(_translate("PDRMainWindow", "Project DIRector", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PDRMainWindow = QtGui.QMainWindow()
    ui = Ui_PDRMainWindow()
    ui.setupUi(PDRMainWindow)
    PDRMainWindow.show()
    sys.exit(app.exec_())

