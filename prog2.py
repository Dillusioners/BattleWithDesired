import socket
import platform 
#Function for getting the socket
def hostname_ipaddress_socket():
    try:
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
    except:
        print("There was an error, unable to find Host name and ip address")
    else:
        print(name,ip)

def hostname_ipaddress_platform():
    try:
        name = platform.node()
    except:
        print("There was an error, unable to find Host name and ip address")
    else:
        print(name)

print("------------------MENU---------------------")
print("1.Host name and ip address by using socket")
print("2.Host name and ip address by using platform")


ch = int(input(print("Enter your choice: ")))

if not ch == 1 or not ch == 2:
    print("Enter a valid choice: ")
    ch = int(input("Enter again"))

if ch == 1:
    hostname_ipaddress_socket()

if ch == 2:
    hostname_ipaddress_socket()
    hostname_ipaddress_platform()

