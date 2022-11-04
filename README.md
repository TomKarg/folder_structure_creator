# folder_structure_creator
This Project provides a GUI to create a folder structure based on a predefined source folder.


## Description of the Project

### First Page
On the first Page the User has to Input the following Information

#### Input
- Source Folder with the Folder/File Structure that should be copied
- Year of the Project
- Projectnumber
- Projectname

Based on the Input a different folder Structure will later be created.
After pressing the "Confirm" button the Second Page will now be active. 
In the case of missing or wrong Input, the User will get a warning and has to change the Information
before he can advance to the second Page. 


### Second Page

On the second page the target folder, into which the Folder Structure should be created, has to be selected.
Additionaly the User can choose which folders/files should be copied into the target location.

By Pressing the "Create" Button the new folder structure will be created.

The Target location will be the following.

### (Targetfolder path)/(Year)/(projectnumber_projectname)/

If this exact location already exists the User will be asked, if he wants to add the missing folders/files.

#### User Input: Yes we want to add the missing folders/files
The User clicked the "Yes" Button. Now the Program will check which folders were selected by the User.
If any of the selected folders dont exist in the Target, then they will be created.
If they already exist, the Program checks inside of the folders if any files/folders are missing and adds them.

##### Existing files will not be updated!
##### Nothing will be deleted in this Process

#### User Input: No we dont want to add the missing folders/files
The User clicked the "No" Button. The Program will go back to the first Page, so the User can change the Input if the wishes. 


## Config File
The config file is used to prefil the Program with Information.

### Sourcepath
The Path of the folder which should be used as baseline for the folder structure
This path will prefill the Source path on page 1.

### Targetpath
The basepath to which the copy operation should be executed to.
This path will prefill the Target path on page 2.

### Logo
Link to the Logo. The logo will be used on the Mainpage and as Windowicon.

### Language GER
Setting to change between English and German language

false -> Language is set to English

true -> Language is set to German

## Motivation 
In the past i had to work with similar tools which were implemented in VBA.
As i had no prior knowledge of VBA, the attempt to debug this code 
felt closer to suffering than coding to me.

Prior to this project i had limited experience with shutil and PyQt. 
So i challenged myself to create this in Python and get better with the libraries. 


## Future Plans
- Fix the GUI and make it good looking.
- Make it possible to have a background image.
- Automated Testing for the Tool (practice for myself)
- Fix various small bugs. 
