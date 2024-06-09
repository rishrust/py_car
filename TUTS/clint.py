import socket
from time import sleep

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

server=("inspirion", 9214)
s.connect(server)

# message = str(input("Enter messag ")).encode()
# s.send(message)


while 1:
    try:
        message = str(input("Enter messag ")).encode()
        s.send(message)
    except:
        # sleep(1)
        print("sme error ")
        break


