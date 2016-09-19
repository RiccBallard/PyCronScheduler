#!/usr/bin/env python

import os
import glob

from PyQt4 import QtCore, QtGui
from GUIs import Ui_aboutDialog, Ui_MainWindow
from PyQt4.QtGui import QListWidgetItem, QStandardItemModel, QStandardItem
from PyQt4.Qt import QModelIndex
from llib.tagNamesDialog import TagNames

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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_signals()
        self.initialize_project()
        
        
    def initialize_project(self):
        print 'initializing'
        prj_files = glob.glob( '../data/*.conf')
        
        self.projects = {}
        
        for config in prj_files:
            path_fname = list(os.path.split(os.path.abspath(config)))
            config_name = os.path.splitext(path_fname[1])[0]
            self.projects[config_name] = path_fname
 
        self.prj_model = QStandardItemModel(self.ui.ProjectsListView)           
        for prj_name in self.projects:
            item = QStandardItem(prj_name)
            print "Adding " + prj_name
            self.prj_model.appendRow(item)
            
        self.ui.ProjectsListView.setModel(self.prj_model)      
        self.ui.ProjectsListView.selectionModel().select(self.prj_model.index(0, 0, QModelIndex()),
                                                         QtGui.QItemSelectionModel.Select)
        
        
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
        dlg = QtGui.QDialog()
        TagNames(dlg)
        dlg.show()
        dlg.exec_()
        


    def delete_prj(self):
        print "Delete"
        
                
    def do_save(self):
        print "save it"


    def do_save_as(self):
        print "save as this"
    
    
    def prj_menu(self, QPos):
        self.listMenu = QtGui.QMenu(self.ui.ProjectsListView)

        menu_item = self.listMenu.addAction("New")        
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.new_prj) 
        
        menu_item = self.listMenu.addAction("Save")
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.do_save) 

        menu_item = self.listMenu.addAction("Save as")            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.do_save_as) 

        menu_item = self.listMenu.addAction("Delete")
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_prj) 

        parentPosition = self.ui.ProjectsListView.mapToGlobal(QtCore.QPoint(0, 0))        
        self.listMenu.move(parentPosition + QPos)

        self.listMenu.show() 


    def setup_signals(self):
        # will be setting up slots and signals here
        print "setting up slots and signals"
        QtCore.QObject.connect(self.ui.actionAbout,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.show_about)
        
        QtCore.QObject.connect(self.ui.actionNew,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.new_prj)
        
        QtCore.QObject.connect(self.ui.actionSave,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.do_save)

        QtCore.QObject.connect(self.ui.actionSave_as,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.do_save_as)
                
        QtCore.QObject.connect(self.ui.actionHelp,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.show_help)
                
        self.ui.ProjectsListView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.ProjectsListView.connect(self.ui.ProjectsListView,QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), 
                                      self.prj_menu)
        
    
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec_())


