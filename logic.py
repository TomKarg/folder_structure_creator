#V0 Create the python file
import sys
from datetime import date

from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QTreeWidgetItem
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
        self.show()
        self.btn_folder.clicked.connect(self.chooseDirectory)
        self.btn_p1_next.clicked.connect(self.checkInput)
        self.btn_p2_cancel.clicked.connect(self.pageBack)
        self.btn_p2_create.clicked.connect(self.createFolders)



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
            self.stackedWidget.setCurrentIndex(1)
            self.createTree(self.lineEdit_folder.text())

        else:
            error_message = QMessageBox(self)
            error_message.setWindowTitle("Input device error")
            error_message.setText("Invalid Input please check again!")
            error_message.show()

    def pageBack(self):
        self.stackedWidget.setCurrentIndex(0)


    #functionality of createTree but with another layer of children
    def createTreeDeep(self, folder : str):
        self.treeWidget.clear()
        #self.treeWidget.setHeader(0, "Strukturauswahl")
        ele = os.listdir(folder)
        for dr in ele:
            parent = QTreeWidgetItem(self.treeWidget)
            parent.setFlags(parent.flags() |Qt.ItemFlag.ItemIsAutoTristate | Qt.ItemFlag.ItemIsUserCheckable)
            parent.setText(0, f'{dr}')
            #parent.setCheckState(0, Qt.CheckState.Unchecked)
            #parent.setFlags(parent.flags() | Qt.ItemFlag.ItemIsTristate | Qt.ItemIsUserCheckable)
            #parent.setFlags(parent.flags() | Qt.ItemFlag.ItemIsUserTristate | Qt.ItemFlag.ItemIsUserCheckable)

            fold = os.path.join(folder, dr)
            for dp in os.listdir(fold):
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                child.setText(0, f'{dp}')
                child.setCheckState(0, Qt.CheckState.Unchecked)

    #use this function to create just one layer of items
    def createTree(self, folder : str):
        self.treeWidget.clear()
        # self.treeWidget.setHeader(0, "Strukturauswahl")
        ele = os.listdir(folder)
        for dr in ele:
            parent = QTreeWidgetItem(self.treeWidget)
            parent.setFlags(parent.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            parent.setText(0, f'{dr}')
            parent.setCheckState(0, Qt.CheckState.Unchecked)

    def printChecked(self):
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            print(f'Text: {item.text(0)} Checked: {item.checkState(0)}')

    def createFolders(self):
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        path = self.createPath()
        for i in range(child_count):
            item = root.child(i)
            print(f'Text: {item.text(0)} Checked: {item.checkState(0)}')
            if(item.checkState(0) == Qt.CheckState.Checked):
                print("testprint")
                src = os.path.join(self.lineEdit_folder.text(), item.text(0))
                if(os.path.isdir(src)):
                    crt = os.path.join(path, item.text(0))
                    os.makedirs(crt)
                    shutil.copytree(src, os.path.join(path, item.text(0)), dirs_exist_ok=True)
                else:
                    shutil.copy2(src, path)

    def createPath(self):
        ending = f'{self.lineEdit_number.text()}_{self.lineEdit_name.text()}'
        fin = os.path.join(target, self.lineEdit_year.text(), ending)
        return fin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    logic = logicWindow()
    sys.exit(app.exec())