# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rballard/work/workspace/ProjectDirector/src/UIs/TagNamesDialog.ui'
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

class Ui_TagNameDialog(object):
    def setupUi(self, TagNameDialog):
        TagNameDialog.setObjectName(_fromUtf8("TagNameDialog"))
        TagNameDialog.resize(387, 379)
        self.verticalLayout = QtGui.QVBoxLayout(TagNameDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TagNameListView = QtGui.QListView(TagNameDialog)
        self.TagNameListView.setObjectName(_fromUtf8("TagNameListView"))
        self.verticalLayout.addWidget(self.TagNameListView)

        self.retranslateUi(TagNameDialog)
        QtCore.QMetaObject.connectSlotsByName(TagNameDialog)

    def retranslateUi(self, TagNameDialog):
        TagNameDialog.setWindowTitle(_translate("TagNameDialog", "Create Tag Names", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TagNameDialog = QtGui.QDialog()
    ui = Ui_TagNameDialog()
    ui.setupUi(TagNameDialog)
    TagNameDialog.show()
    sys.exit(app.exec_())

