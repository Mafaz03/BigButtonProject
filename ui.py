from PyQt5 import QtCore, QtGui, QtWidgets 
import sys 
import os
import subprocess
import pwd

class Ui_MainWindow(object): 

	def setupUi(self, MainWindow): 
		MainWindow.resize(500, 500) 
		self.centralwidget = QtWidgets.QWidget(MainWindow) 
		
		# adding pushbutton 
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(50, 150, 200, 100)) 
		self.pushButton.resize(400,200)
		self.pushButton.setText("RESET INK PAD")

		# adding signal and slot 
		self.pushButton.clicked.connect(self.changelabeltext) 
	
		self.label = QtWidgets.QLabel(self.centralwidget) 
		self.label.setGeometry(QtCore.QRect(50, 150, 200, 100))	
		self.label.resize(400,100) 

		self.pushButton.raise_()

		# keeping the text of label empty before button get clicked 
		self.label.setText("")	 
		
		MainWindow.setCentralWidget(self.centralwidget) 
		self.retranslateUi(MainWindow) 
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow): 
		_translate = QtCore.QCoreApplication.translate 
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow")) 
		self.pushButton.setText(_translate("MainWindow", "RESET INK PAD")) 
		
	def changelabeltext(self): 

		# changing the text of label after button get clicked 
		path = os.getcwd()
		command = f"sudo python3 {path}/script.py"
		output = subprocess.run(command, shell=True, capture_output=True, text=True)
		if output.returncode != 0: self.label.setText(output.stderr.splitlines()[-1])	 
		else: self.label.setText(output.stdout)	 

		# Hiding pushbutton from the main window 
		# after button get clicked. 
		self.pushButton.hide() 

if __name__ == "__main__": 
	app = QtWidgets.QApplication(sys.argv) 
	
	MainWindow = QtWidgets.QMainWindow() 
	ui = Ui_MainWindow() 
	ui.setupUi(MainWindow) 
	MainWindow.show() 

	sys.exit(app.exec_()) 
