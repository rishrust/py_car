from pynput import keyboard
import socket

# Define the IP address and port of the NodeMCU
NODEMCU_IP = '192.168.0.101'  # Replace with your NodeMCU's IP address
NODEMCU_PORT = 12345

# Define the mapping of keys to LED indices
key_to_led = {
    'w': 2,
    's': 3,
    'a': 0,
    'd': 1
}

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((NODEMCU_IP, NODEMCU_PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        s.sendall(command.encode('utf-8'))

def on_press(key):
    try:
        if key.char in key_to_led:
            led_index = key_to_led[key.char]
            send_command(f'OFF {led_index}')
    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in key_to_led:
            led_index = key_to_led[key.char]
            send_command(f'ON {led_index}')
    except AttributeError:
        pass

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()