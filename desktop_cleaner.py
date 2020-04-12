"""Desktop Cleaner
Simple version. Move this program to the directory that is to be sorted then run it.

Sorts Mac OS screenshots of format e.g 'Screen Shot 2020-03-24 at 9.44.28 pm.png' into a 'Screenshots' Folder

Sorts remaining files by filetype into folders e.g 'cat.jpeg' gets stored into 'jpeg Files' Folder

Incase filenames are already taken in the destination folder, will handle according to user preference e.g keep both, keep all, replace, replace all, skip and cancel

Warning. Test this program works on files that are backed up first as it has the ability to overwrite files.

By Sidney Radwan.
"""

import shutil, os, re

def move_file(name_body,extension,temp_file_path, temp_dir_path,static_replace_all,static_keep_all):
	filename = os.path.basename(temp_file_path)
	intended_file_path = os.path.join(temp_dir_path,filename)

	if os.path.isdir(temp_dir_path) == False:
		os.makedirs(temp_dir_path)

	#runs a check if it exists already!
	if os.path.isfile(intended_file_path) == True and static_replace_all == False and static_keep_all == False:
		while(True):
			user_command = input("File '%s' already exists in intended directory '%s'. Type 'replace', 'replace all', 'keep both', 'keep all', 'skip' or 'cancel' to continue.\n" %(filename , temp_dir_path))				
			if user_command == 'replace' or user_command == 'replace all':
				shutil.move(temp_file_path, intended_file_path)
				if user_command == 'replace all':
					static_replace_all = True
				return static_replace_all,static_keep_all
			elif user_command == 'cancel':
				exit()
			elif user_command == 'skip':
				return static_replace_all,static_keep_all
			elif user_command == 'keep both' or user_command == 'keep all':
				count = 1
				while(True and count<1000):
					new_intended_file_path = os.path.join(temp_dir_path,name_body+'(%s)'%count+extension)
					if os.path.isfile(new_intended_file_path):
						count += 1
					else:	
						shutil.move(temp_file_path, new_intended_file_path)	
						break	
				if user_command == 'keep all':
					static_keep_all = True
				return static_replace_all,static_keep_all	
			else:
				print("Wrong input. Please enter as shown.")
				continue							
	elif static_keep_all == True:
		count = 1
		while(True and count<1000):
			new_intended_file_path = os.path.join(temp_dir_path,mo.group(1)+'(%s)'%count+mo.group(2))
			if os.path.isfile(new_intended_file_path):
				count += 1
			else:	
				shutil.move(temp_file_path, new_intended_file_path)
				return static_replace_all,static_keep_all	
	else:
		shutil.move(temp_file_path, intended_file_path)	
		return static_replace_all,static_keep_all




def main():
	cwd_path = os.getcwd()
	directory_contents = os.listdir(cwd_path)

	screenshots_regex = re.compile(r'(Screen Shot \d\d\d\d-\d\d-\d\d at (\d){1,2}\.\d\d\.\d\d (a|p)m)\.png')
	hidden_files_regex = re.compile(r'^\.(\w)+')
	files_regex = re.compile(r'^(.+)(\.(\w+))$')
	myself_regex = re.compile('desktop_cleaner.py')


	static_replace_all = False
	static_keep_all = False

	for i in directory_contents:

		if screenshots_regex.search(i) != None:
			mo = screenshots_regex.search(i)
			name_body = mo.group(1)
			extension = '.png'
			temp_file_path = os.path.join(cwd_path,i)
			dir = 'Screenshots'
			temp_dir_path = os.path.join(cwd_path,dir)

			static_replace_all,static_keep_all = move_file(name_body,extension,temp_file_path, temp_dir_path,static_replace_all,static_keep_all)

#			if os.path.isdir(temp_dir_path) == False:
#				os.makedirs(temp_dir_path)
		
	
#			shutil.move(temp_file_path, temp_dir_path)		
	
		elif os.path.isfile(os.path.join(cwd_path,i)) == True and os.path.isdir(os.path.join(cwd_path,i)) == False and hidden_files_regex.search(i) == None and myself_regex.search(i) == None:
			
			mo = files_regex.search(i)
	
			if mo != None:
				temp_file_path = os.path.join(cwd_path,i)
				name_body = mo.group(1)
				extension = mo.group(2)
				dotless_extension = mo.group(3)
				temp_folder_name = dotless_extension + ' Files'
				temp_dir_path = os.path.join(cwd_path,temp_folder_name)

								
				static_replace_all,static_keep_all = move_file(name_body,extension,temp_file_path, temp_dir_path,static_replace_all,static_keep_all)
				
		else:
			continue

main()
