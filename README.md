Files containing the latest version of the desktop cleaner project.

Desktop Cleaner

Simple version: Move this program to the directory that is to be sorted then run it.

Sorts Mac OS screenshots of format e.g 'Screen Shot 2020-03-24 at 9.44.28 pm.png' into a 'Screenshots' Folder

Sorts remaining files by filetype into folders e.g 'cat.jpeg' gets stored into 'jpeg Files' Folder

Incase filenames are already taken in the destination folder, will handle according to user preference 
provided in terminal e.g keep both, keep all, replace, replace all, skip and cancel

Future updates will allow user to drag program to a directory and double-click it to run and sort the directory 
it was placed in, and allow the user to pre-specify keywords to sort by or directories to sort.

**Version 2** Program updated to be able to be packaged with pyinstaller into a standalone exe file. Can be
dragged and dropped into any directory or folder and it will sort the files for you. 
Fixed issues with python2 having raw_input() and python3 having input(), and exe having incorrect working directory.
Included is an executable for the program which will work for Mac Os only. Other OS users will still have to manually
run the programs script in their terminal/command prompt.

Warning. Test this program works on files that are backed up first as it has the ability to overwrite files.

Second Warning. This program is yet to be tested on Windows and Linux systems thoroughly so please heed the 
first warning.

By Sidney Radwan.
