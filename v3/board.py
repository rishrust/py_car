from machine import Pin
import socket
from time import time,sleep
# Define GPIO pins for LEDs
led_pins = [16, 5, 14, 12]  # D5 left, D6 right, D0 front, D1 back
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
for i in leds:
    i.on()
# Create a simple TCP server
addr = ('192.168.0.101', 12345)
s = socket.socket()
s.bind(addr)
s.listen(1)
# s.settimeout(1)
print("Listening on port 12345...")


# discard buffer stored while board was sleeping
def discard_data(conn):
    try:
        data = conn .recv(1024)
    except:
        pass



while True:

    conn, addr = s.accept()
      
    while True:
        data = conn .recv(1024)
        if not data:
            break
        command = data.decode('utf-8')
        
        if command.startswith('ON'):
            print("Motor OFF")
            led_index = int(command.split()[1])
            leds[led_index].on()

           

        elif command.startswith('OFF'):
            print("Motor ON")
            led_index = int(command.split()[1])

            if(led_index == 2 or led_index ==3):
                sleep_duration=0.9
                leds[led_index].off()
                sleep(sleep_duration)
                leds[led_index].on()
                discard_data(conn)
            else:
                leds[led_index].off()

  
    conn.close()