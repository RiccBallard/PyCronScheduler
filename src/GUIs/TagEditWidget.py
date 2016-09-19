# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rballard/work/workspace/ProjectDirector/src/UIs/TagEditWidget.ui'
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

class Ui_ProjectEditForm(object):
    def setupUi(self, ProjectEditForm):
        ProjectEditForm.setObjectName(_fromUtf8("ProjectEditForm"))
        ProjectEditForm.resize(501, 308)
        self.horizontalLayout = QtGui.QHBoxLayout(ProjectEditForm)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.projectListWidget = QtGui.QListWidget(ProjectEditForm)
        self.projectListWidget.setObjectName(_fromUtf8("projectListWidget"))
        self.horizontalLayout_2.addWidget(self.projectListWidget)
        self.TagListWidget = QtGui.QListWidget(ProjectEditForm)
        self.TagListWidget.setObjectName(_fromUtf8("TagListWidget"))
        self.horizontalLayout_2.addWidget(self.TagListWidget)
        self.dataListWidget = QtGui.QListWidget(ProjectEditForm)
        self.dataListWidget.setObjectName(_fromUtf8("dataListWidget"))
        self.horizontalLayout_2.addWidget(self.dataListWidget)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ProjectEditForm)
        QtCore.QMetaObject.connectSlotsByName(ProjectEditForm)

    def retranslateUi(self, ProjectEditForm):
        ProjectEditForm.setWindowTitle(_translate("ProjectEditForm", "Project Edit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ProjectEditForm = QtGui.QWidget()
    ui = Ui_ProjectEditForm()
    ui.setupUi(ProjectEditForm)
    ProjectEditForm.show()
    sys.exit(app.exec_())

