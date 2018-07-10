 
print ("Welcome to Omar's auto mac changer!")
intName="eth0"
numTimes=3
choice=0
ip="8.8.8.8"
print ("Default Options are: \nInterface= eth0\nIterations: 3\nTest IP: 8.8.8.8")
choice=raw_input("Enter 0 to continue with default settings, or 1 to customize: ")
if (choice == 1) :
        intName=raw_input("Please enter the name of the interface: ")
        choice=raw_input("Please enter the number of times to change the address: ")
        ip=raw_input("Please entter the IP to ping: ")
 
pingCommand = "ping " +  ip
macCommand = "macchanger -r " + intName
mac2="macchanger -r eth0"
 
import subprocess
for x in range (0,numTimes):
 
        print "\n\n\n\n*************************************************\nTesting MAC Address number: ", (x+1)
        print ( "\n")
        print ("Randomizing MAC:\n=======================================================")
        subprocess.call(["macchanger", "-r", intName])
        print ("\n")
        print ("Pinging:\n=======================================================")
        subprocess.call(["ping", ip, "-c", "5"])
 
print ("Thank you!")
