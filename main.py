#   Disclaimer!
# This is just a program to calculate taxes in Mexico NOT use it in your particular life
# because every country and situation is different

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel#, QPushButton, QMessageBox 
from PyQt5.QtGui import QFont
class MainWindow(QMainWindow):
#This is the constructor of the main window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RESICO taxes") #Use self.<the command that you'll use> In this case to set the title of the main window
        self.setGeometry(0,0,1000,600) #Set geometry has 4 arguments the first 2 is x and y possision on the screen and the other 2 is the size of the window
        
        label = QLabel("TEST", self) #This is to add labels
        label.setFont(QFont("Times New Roman", 30)) #Set the font and the size of it
        label.setGeometry(500, -200, 100, 500) #Set the geometry of the label x,y position on the screen and the size
        label.setStyleSheet("color: red;")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()