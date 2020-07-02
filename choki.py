#main program
#this program is been wrote using python 
#the program been wrote by choki fans 
#will also execute another python command 
import os
import subprocess
from subprocess import PIPE, run 

os.system("cls") #clear scree in cmd 
print ("WELCOME TO CHOKI FANS PROGRAMS!!")
print ("This program is wrote using python")
print ("Program Options")
print ("[1] - Network Automation Program (Ping/Ipconfig)")
print ("[2] - Automation Program (Subnet Calculator)")
x = input ("Options : ")
if x == "1":
    print ("Network Automation Program (Ping/ipconfig)")
    print ("[1] - Ping")
    print ("[2] - Ipconfig/all")
    y = input ("Options : ")
    if y == "1":
        print ("Topic : Ping command automation program")
        x = input("Enter Address/Host name : ")
        our_command = "ping" + " " + x

        our_process = subprocess.Popen(our_command, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

        result, error = our_process.communicate()

        result = result.strip()
        error = error.strip()

        print ("\nResult of ping command\n")
        print ("-" * 22)
        print (result.decode('utf-8'))
        print (error.decode('utf-8'))
        print ("-" * 22)
        
    elif y == "2":
        print ("Topic : Ipconfig/all command automation program")

        our_command = "ipconfig /all"

        result = run(our_command, stdout = PIPE, stderr = PIPE, universal_newlines = True)

        print (result.stdout, result.stderr)
        execfile('file.py')
    else:
        print ("ERROR INPUT!")
elif x == "2":
    print ("Automation Program (Subnet Calculator)")
    os.system('cmd /c "python project.py "') #will execute the command by cmd to run another python command 
                                             #here also using the automation coding in executing command 
else:
    print ("Ughmm..wrong input!")