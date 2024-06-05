import socket
from time import sleep
from machine import Pin, reset
import time

# Define pin numbers
s1 = 16
s2 = 5
s3 = 14
s4 = 12

# Initialize pins as outputs
sw1 = Pin(s1, Pin.OUT)  # left
sw2 = Pin(s2, Pin.OUT)  # right
sw3 = Pin(s3, Pin.OUT)  # front
sw4 = Pin(s4, Pin.OUT)  # back

switch_pins = [sw1, sw2, sw3, sw4]

# Set all pins to ON state
for i in switch_pins:
    i.on()

HOST = "192.168.0.130"
PORT = 9589
commands = {'w': [sw3], 's': [sw4], 'a': [sw1], 'd': [sw2]}

# Create and configure the socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def conn(c):
    while True:
        try:
            c.connect((HOST, PORT))
        except OSError:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print("Connecting...")
            sleep(2)
            continue
        else:
            print("Connected to PC")
            return c

# Establish the connection
c = conn(c)

steer = {'a': False, 'd': False}




while True:
    try:
        data = c.recv(1024)
        data = data.decode()
        print(data)
        
        if len(data) >= 1:
            # Steering control
            if data[0] in ['a', 'd']:
                i = commands[data[0]][0]
                if not steer[data[0]]:
                    steer[data[0]] = True
                    i.off()
                else:
                    steer[data[0]] = False
                    i.on()
            
            # Clear steering
            elif data[0] == 'c':
                commands['a'][0].on()
                commands['d'][0].on()
                
            elif data[0] == 's':
                i = commands[data[0]][0]
                i.off()
                time.sleep(0.2)
                i.on()
                
            # Forward 
            else:
                i = commands[data[0]][0]
                i.off()
                time.sleep(0.2)
                i.on()
        
    except Exception as e:
        print(f"Some error occurred: {e}")
        reset()
