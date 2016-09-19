# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rballard/work/workspace/ProjectDirector/src/UIs/TagEditDialog.ui'
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

class Ui_EditTagDataDialog(object):
    def setupUi(self, EditTagDataDialog):
        EditTagDataDialog.setObjectName(_fromUtf8("EditTagDataDialog"))
        EditTagDataDialog.resize(400, 300)

        self.retranslateUi(EditTagDataDialog)
        QtCore.QMetaObject.connectSlotsByName(EditTagDataDialog)

    def retranslateUi(self, EditTagDataDialog):
        EditTagDataDialog.setWindowTitle(_translate("EditTagDataDialog", "Edit Tag Data", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditTagDataDialog = QtGui.QDialog()
    ui = Ui_EditTagDataDialog()
    ui.setupUi(EditTagDataDialog)
    EditTagDataDialog.show()
    sys.exit(app.exec_())

