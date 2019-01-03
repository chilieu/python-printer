import os
import time
import glob

try:
	
	#file location
	floc = 'C:/Users/chilieu.me/Desktop/python-printer/';
	#set current location
	os.chdir(floc)
	#capture input of print
	x = 0
	
	#os.startfile('C:/Users/ChiLT/Desktop/python-printer/order-123.txt', 'print')
	
	for file in glob.glob('order-*.txt'):
		if( file != ''):
			os.startfile(file, 'print')
			print('Printing file >> ' + str(file))
			x = x + 1
			#sleep for 2 second for printing
			time.sleep(2)
			
			#rename after printing
			newname = file.replace('.txt', '.log')
			os.rename(file, newname)
			
	print('No. of file printed > ' + str(x))

except Exception as a:
	print (a)
