import os
while 1:
    # Ask the user for a name.
	code = input('enter the script you want to run: ')
	print 'the entered script is : ', code
	if code == 'hello1':
		os.system("python hello1.py")
	elif code == 'hello2':
		os.system("python hello2.py")
	elif code == 'hello3':
		os.system("python hello3.py")

