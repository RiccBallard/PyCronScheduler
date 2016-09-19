'''
Created on Sep 12, 2016

@author: rballard
'''

from GUIs.TagNamesDialog import Ui_TagNameDialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QStandardItemModel, QStandardItem
from PyQt4.Qt import QModelIndex

class TagNames(Ui_TagNameDialog):
    '''
    classdocs
    '''
    __tag_names = {}    
    __tag_model = None
    
    
    def __init__(self, me):
        print "initializing dialog"
        Ui_TagNameDialog.__init__(self)
        self.setupUi(me)
        self.tag_menu = QtGui.QMenu(self.TagNameListView)
        
        self.addItem("one")
        self.addItem("two")
        self.addItem("three")
        self.TagNameListView.setModel(self.__tag_model)      
        self.TagNameListView.selectionModel().select(self.__tag_model.index(0, 0, QModelIndex()),
                                                         QtGui.QItemSelectionModel.Select)
        self.init_signals()
              

    def on_menu(self, QPos):
        print "on menu"        
        self.tag_menu.clear()
        
        menu_item = self.tag_menu.addAction("New")        
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.add_tag) 
        
        menu_item = self.tag_menu.addAction("Edit")            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.edit_tag) 

        menu_item = self.tag_menu.addAction("Delete")
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_tag) 

        parentPosition = self.TagNameListView.mapToGlobal(QtCore.QPoint(0, 0))        
        self.tag_menu.move(parentPosition + QPos)

        self.tag_menu.show()
        
    
    def init_signals(self):
        print "Setting up signals"
        
        self.TagNameListView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        if self.TagNameListView.connect(self.TagNameListView, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.on_menu):
            print "menu connected"
        else:
            print "menu failed"


    def add_tag(self):
        print "adding tag"


    def edit_tag(self):
        print "edit tag"
        
        
    def delete_tag(self):
        print "delete tag"


    def addItem(self, new_item):
        if not self.__tag_model:
            print "setting up model"
            self.__tag_model = QStandardItemModel(self.TagNameListView)           

        item = QStandardItem(new_item)
        print "Adding " + new_item
        self.__tag_model.appendRow(item)


    def get_tag_names(self):
        return self.__tag_names


    def set_tag_names(self, value):
        self.__tag_names = value


    def del_tag_names(self):
        del self.__tag_names

    tag_names = property(get_tag_names, set_tag_names, del_tag_names, "tag_names's docstring")
    
    