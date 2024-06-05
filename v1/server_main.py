# echo-server.py

import socket
import time
import getch


HOST = ""  # Standard loopback interface address (localhost)
PORT = 9589  # Port to listen on (non-privileged ports are > 1023)
commands = {'w':'forawrd','s':'back','a':'left','d':'right','c':'clear_steer'}






try:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        dat = getch.getch()
        if(dat=='q'): #for closing server gracefully
            conn.close()
            s.close()
            print("closing")
            exit()
        if dat in commands: #for sending correct commands 
            conn.sendall(dat.encode('utf-8'))
            print(commands[dat])
        time.sleep(0.01)

except:
    print("failure")


# try:
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #to reuse same address/ and prevent waiting time
#         s.bind((HOST, PORT))
#         s.listen()
#         conn, addr = s.accept()
#         with conn:
#             print(f"Connected by {addr}")
#             while True:
#                 dat = getch.getch()
#                 if(dat=='q'): #for closing server gracefully
#                     conn.close()
#                     s.close()
#                     print("closing")
#                     exit()
#                 if dat in commands: #for sending correct commands 
#                     conn.sendall(dat.encode('utf-8'))
#                     print(commands[dat])
#                 time.sleep(0.01)
                
                    
# except Exception as e:
#     s.close()
#     print(e)
#     exit()
