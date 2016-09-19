'''
Created on Sep 12, 2016

@author: rballard
'''

from GUIs import Ui_ProjectEditForm
from PyQt4 import QtCore, QtGui
import glob
import os
import json
from PyQt4.QtGui import QInputDialog


#class ProjectWindow(QtGui.QWidget, Ui_ProjectEditForm):
class ProjectWindow(QtGui.QWidget):
    '''
    classdocs
    '''
    __projects     = {}
    __tagnames     = {}
    __props        = {}
    __project_data = {}
    __data_dir     = '../data/'
    __fileio       = False
    
    def __init__(self, widget=None):
        print "initializing dialog"
        super(ProjectWindow, self).__init__()
                    
        self.ui = Ui_ProjectEditForm()
        self.ui.setupUi(self)
        self.prj_listMenu=None
        self.tag_menu=None
        self.data_listMenu=None
        
        self.init_signals()
        self.load_projects()
        self.show()
              
    def load_projects(self):
        print "Loading projects"
        self.__fileio = True
        prj_files = glob.glob( self.__data_dir + '*.conf')
        
        for config in prj_files:
            path_fname = list(os.path.split(os.path.abspath(config)))
            config_name = os.path.splitext(path_fname[1])[0]
            # config contains relative path and filename path_fname item 0 contains full path and item 1 contains filename 
            self.__projects[config_name] = path_fname[0] + "/" + path_fname[1]  
            
        first_item=None
        for prj_name in self.__projects:
            
            print "Adding " + prj_name
            listitem = self.ui.projectListWidget.addItem(prj_name)
            if not first_item:
                first_item = listitem
                
        self.ui.projectListWidget.setCurrentRow(0)
        self.__fileio = False

        
    def on_prj_menu(self, QPos):
        print "on prj menu"        
        self.prj_listMenu = QtGui.QMenu(self.ui.projectListWidget)
        
        if self.tag_menu:
            self.tag_menu.clear() 
        
        menu_item = self.prj_listMenu.addAction("New Project")        
        self.ui.projectListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.add_prj) 
        
#         menu_item = self.prj_listMenu.addAction("Edit Project")            
#         self.ui.projectListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.edit_) 

        menu_item = self.prj_listMenu.addAction("Delete Project")
        self.ui.projectListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_prj) 

        parentPosition = self.ui.projectListWidget.mapToGlobal(QtCore.QPoint(0, 0))        
        self.prj_listMenu.move(parentPosition + QPos)

        self.prj_listMenu.show()
        

    def on_tag_menu(self, QPos):
        print "on tag menu"        
        self.tag_menu = QtGui.QMenu(self.ui.TagListWidget)
        if self.tag_menu:
            self.tag_menu.clear() 

        if self.data_listMenu:
            self.data_listMenu.clear() 
        
        menu_item = self.tag_menu.addAction("New Tag Name")        
        self.ui.TagListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.add_tag) 
        
#         menu_item = self.tag_menu.addAction("Edit Project")            
#         self.ui.TagListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.edit_tag) 

        menu_item = self.tag_menu.addAction("Delete Tag Name")
        self.ui.TagListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_tag) 

        parentPosition = self.ui.TagListWidget.mapToGlobal(QtCore.QPoint(0, 10))        
        self.tag_menu.move(parentPosition + QPos)

        self.tag_menu.show()


    def on_tag_prop_menu(self, QPos):
        print "on prop menu"        
        self.data_listMenu = QtGui.QMenu(self.ui.dataListWidget)
        
        menu_item = self.data_listMenu.addAction("New Property")        
        self.ui.dataListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.add_prop) 
        
        menu_item = self.data_listMenu.addAction("Edit Property")            
        self.ui.dataListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.edit_prop) 

        menu_item = self.data_listMenu.addAction("Delete Property")
        self.ui.dataListWidget.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_prop) 

        parentPosition = self.ui.dataListWidget.mapToGlobal(QtCore.QPoint(0, 0))        
        self.data_listMenu.move(parentPosition + QPos)

        self.data_listMenu.show()

    
    def init_signals(self):
        print "Setting up signals"
        
#        self.ui.projectListWidget.itemActivated.connect(self.project_changed)
        self.ui.projectListWidget.currentItemChanged.connect(self.project_changed)
        self.ui.TagListWidget.itemActivated.connect(self.tag_name_changed)
        
        self.ui.projectListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        if self.ui.projectListWidget.connect(self.ui.projectListWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.on_prj_menu):
            print "project menu connected"
        else:
            print "menu project failed"

        self.ui.TagListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        if self.ui.TagListWidget.connect(self.ui.TagListWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.on_tag_menu):
            print "tag menu connected"
        else:
            print "tag project failed"
 
        self.ui.dataListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        if self.ui.dataListWidget.connect(self.ui.dataListWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), self.on_tag_prop_menu):
            print "data menu connected"
        else:
            print "data project failed"

    def project_changed(self, item):
        if self.__fileio:
            return
        
        current_project = str(item.text())
        self.__fileio = True
        print "Project now " + current_project
        if not current_project in self.__projects:
            return
        
        filename = str(self.__projects[current_project]) 
        print "Loading up project " + filename
        with open(filename, 'r') as json_data:
            print json_data
            if not json_data:
                return
            try:
                self.__project_data[current_project] = json.load(json_data)
            except:
                print "bad json load"
            
            
            self.ui.TagListWidget.clear()
            for tagname in self.__project_data[current_project]:
                self.ui.TagListWidget.addItem(tagname)

            self.ui.dataListWidget.setCurrentRow(0);
            self.tag_name_changed(self.ui.TagListWidget.currentItem());

        self.__fileio = False
        

    def tag_name_changed(self, item):
        print "Tag Name now " + str(item.text())
        if self.__fileio:
            return
        
        self.ui.dataListWidget.clear()
        
        current_project = self.ui.projectListWidget.currentItem().text()
        tagname = self.ui.TagListWidget.currentItem().text()
        data = self.__projects[current_project]
        
        for prop_name in data[tagname]['properties']:
            item =  QtGui.QListWidgetItem()
            item.setText(prop_name)
            self.ui.dataListWidget.addItem(item)
        
        self.ui.dataListWidget.setCurrentRow(0)
        
    def add_prj(self):
        print "adding project"
        self.__fileio = True
        proj_name, ok = QInputDialog.getText(self, 'Add Project', 'Enter Project Name:')
        if ok:
            self.ui.TagListWidget.clear()
            self.ui.dataListWidget.clear()
            
            self.__projects[str(proj_name)] = self.__data_dir + proj_name + ".conf"
            print "hmmm" + str(self.__projects)
            item =  QtGui.QListWidgetItem()
            item.setText(proj_name)
            self.ui.projectListWidget.addItem(item)
            count = self.ui.projectListWidget.count()
            self.ui.projectListWidget.setCurrentRow(count-1)
            self.save_project()
            
        self.__fileio = False
        
        
    def add_tag(self):
        print "adding tag"
        
        tagname, ok = QInputDialog.getText(self, 'Add Tag Name', 'Enter Name:')
        if ok:
            self.ui.TagListWidget.addItem(tagname)
            count = self.ui.TagListWidget.count()
            self.ui.TagListWidget.setCurrentRow(count-1)
            self.__fileio = True
            self.save_project()
            self.__fileio = False

    def add_prop(self):
        print "adding property"

        prop_name, ok = QInputDialog.getText(self, 'Add Tag names property', 'Enter Property:')
        if ok:
            self.ui.dataListWidget.addItem(prop_name)
            count = self.ui.dataListWidget.count()
            self.ui.dataListWidget.setCurrentRow(count-1)
            self.__fileio = True
            self.save_project()
            self.__fileio = False


    def edit_prop(self):
        print "edit property"
        
    def delete_prj(self):
        print "delete project"

    def delete_tag(self):
        print "delete tag"
        
    def delete_prop(self):
        print "delete property"

    def save_project(self):                    
            
        current_project = str(self.ui.projectListWidget.currentItem().text())
        print "saving project: " + current_project
        
        data = {}
        tags_props = {}
        for i in range(self.ui.TagListWidget.count()):
            self.ui.TagListWidget.setCurrentRow(i-1)
            tagname = str(self.ui.TagListWidget.item(i).text())
            tags_props[tagname] = [str(self.ui.dataListWidget.item(i).text()) for i in range(self.ui.dataListWidget.count())]
            
        data[current_project]=tags_props
        
        filename = str(self.__projects[str(current_project)])
        print "filename " + filename
        with open( filename, 'w' ) as outfile:
            json.dump(data, outfile)
    
        self.__project_data[str(current_project)] = data
        
    def load_project_data(self):
        print "loading project data"
        
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ProjectEditForm = QtGui.QWidget()
    prjWin = ProjectWindow()
#    prjWin.show()
    sys.exit(app.exec_())    
    