#V0 Create the python file
import sys
from datetime import date
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QTreeWidgetItem
from PyQt6.QtGui import QIcon
from startWin import Ui_mainWindow
import os
import shutil
import toml

########################################

class logicWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.GER = True
        self.lineEdit_year.setText(str(date.today().year))
        self.btn_folder.clicked.connect(self.chooseDirectory)
        self.btn_folder_target.clicked.connect(self.chooseDirectoryTarget)
        self.btn_p1_next.clicked.connect(self.checkInput)
        self.btn_p2_cancel.clicked.connect(self.pageBack)
        self.btn_p2_create.clicked.connect(self.checkTargetFolder)
        self.path = self.getConfig()
        self.setWindowIcon(QIcon(self.path['logo']))
#        self.setBackground(self.path['bgd'])
        self.GER = self.path['GER']
        if not self.GER:
            self.setLanguageEng()
        self.show()
        self.setupEdit()

    def getConfig(self):
        """Function used to parse over the config.toml file
        Checks the sourcepath and target path.
        Checks the path to the logo and background picture.
        If the path is valid it gets added to the dictionary

        Returns
        -------
        dictionary
            a dictionary that contains the data for folder path and picture path if valid
        """
        path = {'src': '', 'trg': '', 'logo': '', 'bgd': '', 'GER': True}

        try:
            with open('config.toml', 'r') as f:
                ret_toml = toml.load(f)
                if os.path.isdir(ret_toml['path']['source']):
                    path['src'] = ret_toml['path']['source']
                if os.path.isdir(ret_toml['path']['target']):
                    path['trg'] = ret_toml['path']['target']
                if os.path.isfile(ret_toml['picture']['logo']) and self.isPicture(ret_toml['picture']['logo']):
                    path['logo'] = ret_toml['picture']['logo']
                if os.path.isfile(ret_toml['picture']['background']) and self.isPicture(ret_toml['picture']['background']):
                    path['bgd'] = ret_toml['picture']['background']
                #if ret_toml['language']['GER'] != None and ret_toml['language']['GER'] == "False":
                if ret_toml['language']['GER'] == False:
                    path['GER'] = False

            return path

        except:
            if self.GER:
                QMessageBox.about(self, "Fehlerhafe Konfigurationsdatei", "Die config.toml datei ist entweder fehlerhaft oder existiert nicht!")
            else:
                QMessageBox.about(self, "Invalid Configuration file", "The config.toml file is either invalid or does not exist!")
            print(f'path {path}')
            return path

    def setLanguageEng(self):
        self.label_folder.setText("Source folder")
        self.label_year.setText("Year")
        self.label_number.setText("Project number")
        self.label_name.setText("Project name")
        self.btn_folder.setText("Choose")
        self.btn_p1_next.setText("Confirm")
        self.label_target.setText("Target folder")
        self.btn_folder_target.setText("Choose")
        self.btn_p2_create.setText("Create")
        self.btn_p2_cancel.setText("Cancel")


    def isPicture(self, ext) -> bool:
        """Function checks if the input path points to a valid picture file

        Parameters
        ----------
        ext: str
            The path to the picture

        Returns
        -------
        bool
            a bool value that represents if the imput path is a valid picture file or not
        """
        pic = ext.rsplit('.')
        if len(pic) == 2 and pic[1].lower() in ['bmp', 'jpeg', 'jpg', 'gif', 'bmp', 'png', 'tiff']:
            return True
        else:
            return False

    # def setBackground(self, path):
    #     self.stackedWidget.setStyleSheet('background-repeat: no-repeat;')
    #     self.stackedWidget.setStyleSheet('background-position: center;')
    #     self.stackedWidget.setStyleSheet(f'background-image: url({path});')

        #     stylesheet = '''
        #     #mainWindow {
        #         background-image: url(#path);
        #         background-repeat: no-repeat;
        #         background-position: center;
        #     }
        # '''
        # self.setStyleSheet(stylesheet)

    def setupEdit(self):
        self.lineEdit_folder.setText(self.path['src'])
        self.lineEdit_folder_target.setText(self.path['trg'])

    def chooseDirectory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_folder.setText(file)

    def chooseDirectoryTarget(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_folder_target.setText(file)


    def emptyErrorLabels(self):
        """This function clears all the Error messages of our labels"""
        self.label_err_folder.setText("")
        self.label_err_year.setText("")
        self.label_err_number.setText("")
        self.label_err_name.setText("")


    def checkYear(self) -> bool:
        year = self.lineEdit_year.text()
        if year.isnumeric() and int(year) > 0:
            return True
        else:
            if self.GER:
                self.label_err_year.setText("Fehlerhafte Eingabe!")
            else:
                self.label_err_year.setText("Invalid input!")
            self.label_err_year.setStyleSheet('color:red')
            return False

    def checkNr(self) -> bool:
        number = self.lineEdit_number.text()
        if number.isnumeric() and int(number) >= 0:
            return True
        else:
            if self.GER:
                self.label_err_year.setText("Fehlerhafte Eingabe!")
            else:
                self.label_err_year.setText("Invalid input!")
            self.label_err_year.setStyleSheet('color:red')
            return False

    def checkName(self) -> bool:
        name = self.lineEdit_name.text()
        if name.isalpha() and name:
            return True
        else:
            if self.GER:
                self.label_err_year.setText("Fehlerhafte Eingabe!")
            else:
                self.label_err_year.setText("Invalid input!")
            self.label_err_year.setStyleSheet('color:red')
            return False

    def checkFolder(self):
        if self.lineEdit_folder.text() != '':
            return True
        else:
            if self.GER:
                self.label_err_folder.setText("Fehlerhafte Eingabe!")
            else:
                self.label_err_folder.setText("Invalid input!")
            self.label_err_folder.setStyleSheet('color:red')

    def checkInput(self):
        self.emptyErrorLabels()
        if self.checkYear() and self.checkNr() and self.checkName() and self.checkFolder():
            print("Yes sir")
            self.stackedWidget.setCurrentIndex(1)
            self.emptyErrorLabels()
            self.createTree(self.lineEdit_folder.text())

        else:
            if self.GER:
                QMessageBox.about(self, "Fehlerhafte Eingabe", "Die eingegebenen Werte sind nicht g??ltig!")
            else:
                QMessageBox.about(self, "Invalid input", "The entered information is not valid!")


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

            fold = os.path.join(folder, dr)
            for dp in os.listdir(fold):
                child = QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                child.setText(0, f'{dp}')
                child.setCheckState(0, Qt.CheckState.Checked)

    #use this function to create just one layer of items
    def createTree(self, folder : str):
        self.treeWidget.clear()
        ele = os.listdir(folder)
        for dr in ele:
            parent = QTreeWidgetItem(self.treeWidget)
            parent.setFlags(parent.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            parent.setText(0, f'{dr}')
            parent.setCheckState(0, Qt.CheckState.Checked)

    def printChecked(self):
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            print(f'Text: {item.text(0)} Checked: {item.checkState(0)}')

    def checkTargetFolder(self):
        if self.lineEdit_folder_target.text() != '' or os.path.isdir(self.lineEdit_folder_target.text()):
            self.folderCreationLogic()
        else:
            if self.GER:
                QMessageBox.about(self, "Fehlerhafte Eingabe!", "Der Zielordner ist ung??ltig!")
            else:
                QMessageBox.about(self, "Invalid input!", "The target folder is invalid!")


    def folderCreationLogic(self):
        #first lets check if the project folder exists
        if os.path.isdir(self.createPath()):
            print("Folder exists")
            #handle the usecase, when the folder already exists else:
            qm = QMessageBox(self)
            if self.GER:
                ret = qm.question(self, "Ordneroptionen", "M??chten Sie die fehlenden Ordner/Dateien hinzuf??gen?", qm.StandardButton.Yes | qm.StandardButton.No)
            else:
                ret = qm.question(self, "Folder operation", "Do you want to add the missing folders/files?",
                                  qm.StandardButton.Yes | qm.StandardButton.No)
            print(ret.value)
            #if the project folder already exists ask the user what he wants to do
            if QMessageBox.StandardButton.Yes == ret:
                #handle the yes case
                self.createFolders()
                print("clicked yes")
            else:
                #handle the no case
                #?? go back to page one??
                self.stackedWidget.setCurrentIndex(0)
                print("something else")
        elif os.path.isfile(self.createPath()):
            print("File")
            qm = QMessageBox(self)
            ret = qm.question(self, "File with same name as Project folder exists already!", "Do you want to overwrite the existing file?",
                              qm.StandardButton.Yes | qm.StandardButton.No)

            print(ret.value)
            # if a file with the same name already exists ask the user what he wants to do
            if QMessageBox.StandardButton.Yes == ret:
                # handle the yes case
                os.remove(self.createPath())
                self.createFolders()
                print("clicked yes")
            else:
                # handle the no case
                self.stackedWidget.setCurrentIndex(0)
                print("something else")

        else:
            print("Folder doesnt exist")
            self.createFolders()

    def createFolders(self):
        root = self.treeWidget.invisibleRootItem()
        child_count = root.childCount()
        path = self.createPath()
        name = []
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(child_count):
            item = root.child(i)
            print(f'Text: {item.text(0)} Checked: {item.checkState(0)}')
            if(item.checkState(0) == Qt.CheckState.Checked):
                src = os.path.join(self.lineEdit_folder.text(), item.text(0))
                if not os.path.exists(os.path.join(path, item.text(0))):
                    if os.path.isdir(src):
                        crt = os.path.join(path, item.text(0))
                        os.makedirs(crt)
                        shutil.copytree(src, os.path.join(path, item.text(0)), dirs_exist_ok=True)
                        print("copy dir")
                    else:
                        shutil.copy2(src, path)
                        print("copy file")
                else:
                    if os.path.isdir(src):
                        name.append(item.text(0))
        self.folderLoop(self.lineEdit_folder.text(), name)
        if self.GER:
            QMessageBox.about(self, "Ordnerstruktur erstellt!", "Die Ordnerstruktur wurde erfolgreich erstellt!")
        else:
            QMessageBox.about(self, "Folder structure created!", "The folder structure was successfully created!")

    #go from top to bottom through the folders and check if the folder/file already exists
    #INPUT path - the original path where to loop over the folders
    #INPUT li - the name of the folders which didnt get created fully yet
    def folderLoop(self, path : str, li : list[str]):
        target = self.createPath()
        for name in li:
            fullpath = os.path.join(path, name)
            for root, subdirs, files in os.walk(fullpath, topdown=True):
                dst_dir = root.replace(path, target, 1)
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                for file in files:
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(dst_dir, file)
                    if not os.path.exists(dst_file):
                        shutil.copy2(src_file, dst_file)



    def createPath(self):
        ending = f'{self.lineEdit_number.text()}_{self.lineEdit_name.text()}'
        fin = os.path.join(self.lineEdit_folder_target.text(), self.lineEdit_year.text(), ending)
        return fin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    logic = logicWindow()
    sys.exit(app.exec())