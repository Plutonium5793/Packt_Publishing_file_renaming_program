#!/usr/bin/python3

#Purpose of this program is to rename the goofy format Packt_Publishing is using for their filenames.
''' step 1: read directory
	step 2: read filenames
	step 3: match numbers on code file and title file, then remove them
	step 4: remove all caps from name, and put name on both files.
	step 5: rename them
	
	2016-0724 In service and working
	version 1.00-20160724
	'''
	#!
	
def read_directory(dir_path):
	''' input directory to be read
		output all the filenames in the directory
'''
	contents=[]
	book_file=[]
	code_file=[]
	import os
	import glob
#os.rename('a.txt,'b.kml') renames files
	
	for fname in glob.glob(os.path.join(dir_path, '*.*')):
		if fname[-4:]=='.pdf':
			book_file.append(fname)
		if fname[-4:]=='.zip':
			code_file.append(fname)
		
		#print ("current file is: "+fname)
		fname,fname1=(os.path.split(fname))
		contents.append(fname1)
	#print(code_file[0])
	for item in book_file:
		print (item[2:])
		
		#print (item[0:15])
		#print (str.capitalize(item[16:-4]))
		new_book=str.capitalize(item[16:])
		os.rename(item[2:],new_book)
		print(new_book)
		for item1 in code_file:
			print(item1[2:])
			if item1[0:15]==item[0:15]:
				new_code=str.capitalize(item[16:-4]) + item1[15:]
				os.rename(item1[2:],new_code)
				print(new_code)
#new_book and new_code are the new file names; need to rename files

	return book_file, contents, code_file



if __name__ == "__main__":
	book_file,contents,code_file=read_directory('./')
	'''print(book_file)
	print(' ')
	print(code_file)'''


