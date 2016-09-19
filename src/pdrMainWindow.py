#!/usr/bin/env python

import os
import glob

from PyQt4 import QtCore, QtGui
from GUIs import Ui_aboutDialog, Ui_PDRMainWindow
from PyQt4.QtGui import QMdiSubWindow
from llib import ProjectWindow

'''
Created on Aug 14, 2016

@author: ricc
'''
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
    

class Main(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_PDRMainWindow()
        self.ui.setupUi(self)
        self.initialize_project()
#        self.projectWindow = QMdiSubWindow()
        self.projectWidget = ProjectWindow()

#        self.projectWindow.setWidget(self.projectWidget)
#        self.ui.mdiArea.addSubWindow(self.projectWindow)
#        self.ui.mdiArea.tileSubWindows() 
#        self.projectWindow.setWindowFlags(self.projectWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)
#        self.projectWindow.setWindowFlags(self.projectWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.ui.horizontalLayout.addWidget(self.projectWidget)
        self.setup_signals()
        

    def initialize_project(self):
        print 'initializing'
        prj_files = glob.glob( '../data/*.conf')
        
        self.projects = {}
        
        for config in prj_files:
            path_fname = list(os.path.split(os.path.abspath(config)))
            config_name = os.path.splitext(path_fname[1])[0]
            self.projects[config_name] = path_fname
            
        for prj_name in self.projects:
            print "Adding " + prj_name

            
            
        
    def show_about(self):
        print "its all about me!"
        dlg = QtGui.QDialog()
        ui = Ui_aboutDialog()
        ui.setupUi(dlg)
        dlg.show()
        dlg.exec_()            
            

    def show_help(self):
        print "show Help!"
        pass


    def new_prj(self):
        print "create new tag name"


    def delete_prj(self):
        print "Delete"
        
                
    def do_save(self):
        print "save it"


    def do_save_as(self):
        print "save as this"


    def setup_signals(self):
        # will be setting up slots and signals here
        print "setting up slots and signals"
        
    
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec_())
