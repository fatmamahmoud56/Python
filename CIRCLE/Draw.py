# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 10:45:54 2022

@author: pc
"""
 
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

 
from PyQt5.QtWidgets import QFileDialog,QApplication,QProgressBar,QPushButton,QSpinBox,QComboBox,QTabWidget
from PyQt5.QtGui import QPixmap,QImage
from Circle4 import Ui_MainWindow
import sys
from PIL import Image
from PIL.ImageQt import ImageQt
 
from PyQt5.QtGui import QPixmap,QPainter,QPen
 
from PIL import Image, ImageEnhance
 
from PIL import Image, ImageTk
import turtle,random
import numpy as np 
#app=QApplication(sys.argv)
   


 
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.Enter) 
        self.ui.pushButton_3.clicked.connect(self.tab)
         
         
    def tab(self):
        self.ui.tabWidget.setTabEnabled(0,False)
        
        
        
         

    def Enter(self):
        X=self.ui.lineEdit.text()
        Y=self.ui.lineEdit_2.text()
        self.x1=eval(X)
        self.y1=eval(Y)
        self.Draw()
        
    def Draw(self):
        
            for j in range (15):
                
                colors = ["pink","green","blue","purple","aqua","red","brown1","darkorchid1"]
                theColor = random.choice(colors)
                turtle.color(theColor)
                turtle.penup()
                turtle.goto(random.randrange(self.x1, self.x1+50,  np.abs(self.x1-self.y1)+1), random.randrange(self.y1, self.y1+50,  np.abs(self.x1-self.y1)+1))
                turtle.pendown()
                turtle.circle(self.x1+self.y1)
            turtle.getscreen()

            turtle.getcanvas().postscript(file="duck.eps")
            turtle.done()
            img = Image.open('duck.eps') 
            img.save('myimage.png')
             
         
         
     
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
