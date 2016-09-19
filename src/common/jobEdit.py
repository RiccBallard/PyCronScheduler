'''
Created on Aug 31, 2016

@author: rballard
'''
from PyQt4 import QtCore, QtGui

from GUIs import Ui_JobEditDialog
from crontab import CronTab
from gtk.keysyms import Down


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class JobEdit(QtGui.QDialog, Ui_JobEditDialog):
    '''
    classdocs
    '''


    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.save_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_job)
    
    def set_job_up(self, job ):
        print "editing job " + str(job)
        self.enable_job_checkBox.setChecked(job.is_enabled())
#        self.comment_lineEdit.setText(job.meta)
        dow = job.dow.on()
        hour = job.hour.on()
        min = job.minute.on()
        
        print "dow" + str(dow)
        print "hour " + str(hour)
        print "min " + str(min)
        print "huh"
        
    
    
    def save_job(self):
        print "save job information"
    
    
    def delete_job(self):
        pass
    
        
        
        