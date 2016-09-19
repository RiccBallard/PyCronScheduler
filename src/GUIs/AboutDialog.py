# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rballard/work/workspace/ProjectDirector/src/UIs/AboutDialog.ui'
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

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(231, 170)
        aboutDialog.setMinimumSize(QtCore.QSize(231, 170))
        aboutDialog.setMaximumSize(QtCore.QSize(231, 170))
        self.verticalLayout = QtGui.QVBoxLayout(aboutDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(aboutDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(aboutDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(aboutDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_6 = QtGui.QLabel(aboutDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(aboutDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(aboutDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pushButton = QtGui.QPushButton(aboutDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(aboutDialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), aboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About Go Pro Project", None))
        self.label.setText(_translate("aboutDialog", "Project Director", None))
        self.label_2.setText(_translate("aboutDialog", "V.01a", None))
        self.label_3.setText(_translate("aboutDialog", "Author: ", None))
        self.label_6.setText(_translate("aboutDialog", "Ricc Ballard", None))
        self.label_4.setText(_translate("aboutDialog", "Date:", None))
        self.label_5.setText(_translate("aboutDialog", "09/01/2016", None))
        self.pushButton.setText(_translate("aboutDialog", "Ok", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    aboutDialog = QtGui.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

