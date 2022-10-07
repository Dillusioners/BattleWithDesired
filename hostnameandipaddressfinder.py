import socket
import platform #importing socketing and platform

def hostname_ipaddress_socket():#defining a function for getting hostname and ip by using socket	
	try:
		name = socket.gethostname()
        ip = socket.gethostbyname(socket.gethostname)
    except:
    	print("There was an error, unable to find Host name and ip address")

def hostname_ipaddress_platform():#defining a function for getting hostname by using platform
	try:
		name = platform.node()
	except:
        print("There was an error, unable to find Host name")

print("------------------MENU---------------------")
print("1.Host name and ip address by using socket")
print("2.Host name and ip address by using platform")


ch = int(input(print("Enter your choice: ")))

if !(ch == 1 or ch == 2):
	print("Enter a valid choice: ")
	ch = int(input(print("Enter your choice: ")))

if ch == 1:#checking which function to use
	hostname_ipaddress_socket()

if ch == 2:
	hostname_ipaddress_socket()
	hostname_ipaddress_platform()

print("The hostname of this system is: ", end = " ")
print(name)
print("The ip address of this system is: ", end = " ")
print(ip)



