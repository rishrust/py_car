import socket
from time import sleep

addr = (socket.gethostname(), 9214)
print(socket.gethostname())
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(addr)

s.listen(1)


conn, addr = s.accept()




def discard_sleep_data(conn):
    try:
        data = conn.recv(1024)
    except:
        pass




while True:

    
    data = conn.recv(1024)
    if not data:
        print("clinet dicon\n")
        conn, addr = s.accept()
        print("clinet connected\n")
    message= data.decode('utf-8')
    print(message)
    print("sleeping for some time")
    sleep(6)
    discard_sleep_data(conn)
    
    