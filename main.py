#   Disclaimer!
# I'm usign a virtual enviroment for this project, if you want to run it you might have to install PyQt5
# You can do it by running pip install PyQt5 in your terminal or creating a virtual enviroment as I did it
# If you will crate a vitual enviroment just type python -m venv <name_of_your_enviroment> (python3 -m venv myenv)
# Right after you have to activate it by running source <name_of_your_enviroment>/bin/activate (source myenv/bin/activate)
# This is just a program to calculate taxes in Mexico NOT use it in your particular life
# because every country and situation is different

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton#, QMessageBox 
from PyQt5.QtGui import QFont
class MainWindow(QMainWindow): #This is the constructor of the main window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RESICO V_1.1") #Use self.<the command that you'll use> In this case to set the title of the main window
        self.setGeometry(0,0,500,500) #Set geometry has 4 arguments the first 2 is x and y possision on the screen and the other 2 is the size of the window
        self.statusBar() # I started a status bar
        # --------------Text boxes--------------------------
        self.ivaCausadoTextBox = QLineEdit(self) #This is a text box that we can write
        self.ivaRetenidoTextBox = QLineEdit(self)
        # --------------Buttons-----------------------------
        self.button = QPushButton("Submit", self) #This add a button
        # --------------Labels------------------------------
        self.titlelabel = QLabel("RESICO Taxes calculator", self) #This is to add labels (main title) 
        self.ivaCausadolabel = QLabel("Impuestos trasladados", self)
        self.ivaRetenidolabel = QLabel("Impuestos retenidos", self)
        # --------------Function calls----------------------
        self.initUI() # I'll call the function initUI down below
        
    def initUI(self): #In this function I'll set all UI settings 
        # --------------Text boxes--------------------------
        # Impuestos trasladados settings 
        self.ivaCausadoTextBox.setGeometry(250,81,200,40)
        self.ivaCausadoTextBox.setStyleSheet("font-size: 25px;"
                                            "font-family: Times New Roman")
        # Impuestos retenidos settings
        self.ivaRetenidoTextBox.setGeometry(250,151,200,40)
        self.ivaRetenidoTextBox.setStyleSheet("font-size: 25px;"
                                             "font-family: Times New Roman")        
        # --------------Buttons-----------------------------
        self.button.setGeometry(250,250,200,40)
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Times New Roman")
        self.button.clicked.connect(self.submit)
        # --------------Labels------------------------------
        # Title settings 
        self.titlelabel.setFont(QFont("Times New Roman", 30)) #Set the font and the size of it
        self.titlelabel.setGeometry(50, 10, 400, 50) #Set the geometry of the label x,y position on the screen and the size
        self.titlelabel.setStyleSheet("color: red;")
        # Impuestos trasladados settings 
        self.ivaCausadolabel.setFont(QFont("Times New Roman", 25)) #Set the font and the size of it
        self.ivaCausadolabel.setGeometry(20, 80, 220, 40) #Set the geometry of the label x,y position on the screen and the size
        self.ivaCausadolabel.setStyleSheet("color: black;") 
        # Impuestos retenidos settings
        self.ivaRetenidolabel.setFont(QFont("Times New Roman", 25)) #Set the font and the size of it
        self.ivaRetenidolabel.setGeometry(20, 150, 220, 40) #Set the geometry of the label x,y position on the screen and the size
        self.ivaRetenidolabel.setStyleSheet("color: black;")      

    def submit(self):
        iva_causado = float(self.ivaCausadoTextBox.text())
        iva_retenido = float(self.ivaRetenidoTextBox.text())
        resultado = iva_causado - iva_retenido
        #print(resultado)
        if resultado >= 0:
            self.statusBar().showMessage(f"Impuestos a pagar: {resultado}") #To print the number I dicided to use the status bar but I had to convert the variable to string
        elif resultado < 0:
            self.statusBar().showMessage('Error') #If the condition apply just show a error message on the status bar

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())