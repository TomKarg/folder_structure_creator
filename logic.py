#V0 Create the python file
import sys
from datetime import date
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from startWin import Ui_mainWindow
import os
import shutil


###########################################################
#TESTAREA
YEAR = "2022"
PROJNR = "1337"
PROJNAME = "Test"

srcdir = r'D:\structFolder'
target = r'D:\structTest'
proj = PROJNR + '_' + PROJNAME



targetAdd = os.path.join(target, YEAR)
projpath = os.path.join(PROJNR, PROJNAME)
targetAdd = os.path.join(targetAdd, projpath)

print(targetAdd)

#shutil.copytree(srcdir, targetAdd)
print('Finished execution')

########################################

class logicWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_year.setText(str(date.today().year))
        # self.tabWidget.setTabVisible(0, False)
        # self.tabWidget.setTabVisible(1, False)
        #TODO: Oida was soll der scheiß mit den Tabs die aus dem Bildbereich einfach rausgeschoben wurden
        self.show()
        self.btn_folder.clicked.connect(self.chooseDirectory)
        self.btn_p1_next.clicked.connect(self.checkInput)



    def chooseDirectory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_folder.setText(file)



    def checkYear(self) -> bool:
        year = self.lineEdit_year.text()
        if year.isnumeric() and int(year) > 0:
            return True
        else:
            self.label_err_year.setText("Invalid Input!")
            self.label_err_year.setStyleSheet('color:red')
            return False

    def checkNr(self) -> bool:
        number = self.lineEdit_number.text()
        if number.isnumeric() and int(number) >= 0:
            return True
        else:
            self.label_err_number.setText("Invalid Input!")
            self.label_err_number.setStyleSheet('color:red')
            return False

    def checkName(self) -> bool:
        name = self.lineEdit_name.text()
        if name.isalpha() and name:
            return True
        else:
            self.label_err_name.setText("Invalid Input!")
            self.label_err_name.setStyleSheet('color:red')
            return False

    def checkFolder(self):
        return self.lineEdit_folder.text() != ''

    def checkInput(self):

        if self.checkYear() and self.checkNr() and self.checkName() and self.checkFolder():
            print("Yes sir")
            self.tabWidget.setCurrentIndex(1)

        else:
            error_message = QMessageBox(self)
            error_message.setWindowTitle("Input device error")
            error_message.setText("Invalid Input please check again!")
            error_message.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    logic = logicWindow()
    sys.exit(app.exec())