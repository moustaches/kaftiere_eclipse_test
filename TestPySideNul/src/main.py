'''
Created on 2 mars 2015

@author: moustache
'''

import sys
from PySide import QtGui

class Fenetre(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=None)
        layFenetre = QtGui.QGridLayout()
        self.label=QtGui.QLabel('Bouzin')
        self.boutOk= QtGui.QPushButton("Poum Patapoum", parent=self)
        self.boutQuiter= QtGui.QPushButton("Quiter", parent=self)
        layFenetre.addWidget(self.label,0,0,1,2)  
        layFenetre.addWidget(self.boutOk,1,0,1,1)
        layFenetre.addWidget( self.boutQuiter,1,1,1,1)    
        self.setLayout(layFenetre) 
        self.boutOk.clicked.connect(self.poum) 
        self.boutQuiter.clicked.connect(self.quitter)  
        
    def poum(self):    
        if self.label.text() == "POUM" : self.label.setText("PATAPOUM")
        else : self.label.setText("POUM")

    def quitter(self):
        self.close()

if __name__=="__main__":  
    app = QtGui.QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())