# Desktop Cleaner

By Sidney Radwan

 - Finds and sorts Mac OS screenshots of format e.g 'Screen Shot 2020-03-24 at 9.44.28 pm.png' into a 'Screenshots' Folder

 - Sorts remaining files by filetype into folders e.g 'cat.jpeg' gets stored into 'jpeg Files' Folder

 - Incase filenames are already taken in the destination folder, will handle according to user preference 
provided in terminal e.g keep both, keep all, replace, replace all, skip and cancel

### Simple Method:
Move this program to the directory that is to be sorted then run it with Python.

### Recommended Method: 
Program updated to be able to be packaged with pyinstaller into a standalone executable file. Can be dragged and dropped into any directory/folder and it will sort the CWD's files for you. 

### Notes:

- Fixed issues with python2 having raw_input() and python3 having input(), and exe having incorrect working directory.
- Included is an executable for the program which will work for some MacOS only. Other OS users will still have to manually
run the program's script in their terminal/command prompt or package with pyinstaller.

**Warning** Test this program on files that are backed up first as it has the ability to overwrite files (asks before doing so).
