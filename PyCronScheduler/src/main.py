#!/usr/bin/env python

import os
import glob

from PyQt4 import QtCore, QtGui
from GUIs import Ui_aboutDialog, Ui_MainWindow
from crontab import CronTab
from common import JobEdit


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
        print 'loading crontable for user'
        
        self.crons = {}         
        self.activeCron  = CronTab(user=True)
        self.crons["current"] = self.activeCron
        self.activeJobs = []
        
        for job in self.activeCron:
            self.activeJobs.append(job)
        
        cronfiles = glob.glob( 'data/*.crontab')
        
        for a_cron in cronfiles:
            path_fname = list(os.path.split(os.path.abspath(a_cron)))
            cron_name = os.path.splitext(path_fname[1])[0]
            self.crons[cron_name] = a_cron
            
        for cron_name in self.crons:
            self.ui.cronListWidget.addItem(cron_name)
            
        self.ui.cronListWidget.setCurrentRow(0)
        
    def change_jobs(self):
        new_cron_name = str(self.ui.cronListWidget.currentItem().text())
        print "Selected cron " + new_cron_name
         
        newer_cron = CronTab(tabfile=self.crons[new_cron_name], user=False)
        
        self.ui.jobListWidget.clear()
        
        for job in newer_cron:
            self.ui.jobListWidget.addItem(str(job))
        
        
        
    def show_about(self):
        print "its all about me!"
        aboutDialog = QtGui.QDialog()
        ui = Ui_aboutDialog()
        ui.setupUi(aboutDialog)
        aboutDialog.show()
        aboutDialog.exec_()
            
    
    def new_cron(self):
        print "Create new cron"
                
    
    def do_save(self):
        print "save project!"       
        
            
    def load_cron(self):
        print "Load a existing crontab"       

    
    def show_help(self):
        print "show Help!"
        pass


    def job_list_menu(self, QPos): 
        self.listMenu = QtGui.QMenu()
        menu_item = self.listMenu.addAction("Delete")

        if len(self.crons.keys()) == 0: 
            menu_item.setDisabled(True)
            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_job) 

        menu_item = self.listMenu.addAction("Edit")
        
        if len(self.crons.keys())==0: 
            menu_item.setDisabled(True)
            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.edit_job) 

        menu_item = self.listMenu.addAction("New job")
        
        if len(self.crons.keys())==0: 
            menu_item.setDisabled(True)
            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.new_job) 

        parentPosition = self.ui.cronListWidget.mapToGlobal(QtCore.QPoint(0, 0))        
        self.listMenu.move(parentPosition + QPos)

        self.listMenu.show() 
        

    def delete_job(self):
        print "delete job for cron"
        #  cron.remove( job )
        
    def edit_job(self):
        print "edit job for cron"
        job_editor = JobEdit()
        new_cron_name = str(self.ui.cronListWidget.currentItem().text())
        print "Selected cron " + new_cron_name
         
        newer_cron = CronTab(tabfile=self.crons[new_cron_name], user=False)
        job_selected = str(self.ui.jobListWidget.currentItem().text())
        
        edit_job=None
        for job in newer_cron:
            # cycle thur all jobs finding the selected job this will be passed to the editor
            if str(job) == str(job_selected):
                edit_job = job 
            
        job_editor.set_job_up(edit_job)
        job_editor.exec_()

        
        
    def new_job(self):
        print "create new job for cron"
        
        
    def cron_list_menu(self, QPos): 
        self.listMenu = QtGui.QMenu()
        menu_item = self.listMenu.addAction("Delete")

        if len(self.crons.keys()) == 0: 
            menu_item.setDisabled(True)
            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.delete_cron) 

        menu_item = self.listMenu.addAction("Save Cron")
        
        if len(self.crons.keys())==0: 
            menu_item.setDisabled(True)
            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.save_cron) 

        menu_item = self.listMenu.addAction("New Cron")
        
        if len(self.crons.keys())==0: 
            menu_item.setDisabled(True)
            
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.new_cron) 

        parentPosition = self.ui.cronListWidget.mapToGlobal(QtCore.QPoint(0, 0))        
        self.listMenu.move(parentPosition + QPos)

        self.listMenu.show() 

    def delete_cron(self):
        print "Delete a cron"

        delete_cron_name = str(self.ui.cronListWidget.currentItem().text())
        
        print "saving... " + delete_cron_name        
    
    def save_cron(self):
        print "Save a Cron to file"  # cron.write( 'output.tab' )
        save_cron_name = str(self.ui.cronListWidget.currentItem().text())
        
        print "saving... " + save_cron_name
    
    def setup_signals(self):
        # will be setting up slots and signals here
        print "setting up slots and signals"
        QtCore.QObject.connect(self.ui.actionAbout,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.show_about)
        
        QtCore.QObject.connect(self.ui.actionNew,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.new_cron)
        
        QtCore.QObject.connect(self.ui.actionSave,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.do_save)
                
        QtCore.QObject.connect(self.ui.actionLoad,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.load_cron)

        QtCore.QObject.connect(self.ui.actionHelp,
                               QtCore.SIGNAL(_fromUtf8("activated()")),
                               self.show_help)
        
        self.ui.cronListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.cronListWidget.connect(self.ui.cronListWidget, 
                                       QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), 
                                       self.cron_list_menu)
        
        self.ui.cronListWidget.connect( self.ui.cronListWidget, 
                                        QtCore.SIGNAL("currentItemChanged (QListWidgetItem*,QListWidgetItem*)"),                                       
                                        self.change_jobs )
        

        self.ui.jobListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.jobListWidget.connect(self.ui.jobListWidget, 
                                       QtCore.SIGNAL("customContextMenuRequested(QPoint)" ), 
                                       self.job_list_menu)
        
#         self.ui.jobListWidget.connect(self.ui.cronListWidget, 
#                                        QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)" ), 
#                                        self.job_list_menu)
        

        
        
    
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = Main()
    mainWindow.show()
    sys.exit(app.exec_())


