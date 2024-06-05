import network
import socket
from machine import Pin

# Connect to Wi-Fi
ssid = 'your_SSID'
password = 'your_PASSWORD'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

# Setup LEDs
led1 = Pin(5, Pin.OUT)  # D1
led2 = Pin(4, Pin.OUT)  # D2
led3 = Pin(0, Pin.OUT)  # D3
led4 = Pin(2, Pin.OUT)  # D4

# HTML to serve
html = """<!DOCTYPE html>
<html>
<head>
    <title>LED Control</title>
</head>
<body>
    <h1>LED Control</h1>
    <script>
        document.addEventListener('keydown', function(event) {
            var key = event.key;
            if (key === 'w') {
                toggleLED('1', 'on');
            } else if (key === 'a') {
                toggleLED('2', 'on');
            } else if (key === 's') {
                toggleLED('3', 'on');
            } else if (key === 'd') {
                toggleLED('4', 'on');
            }
        });

        document.addEventListener('keyup', function(event) {
            var key = event.key;
            if (key === 'w') {
                toggleLED('1', 'off');
            } else if (key === 'a') {
                toggleLED('2', 'off');
            } else if (key === 's') {
                toggleLED('3', 'off');
            } else if (key === 'd') {
                toggleLED('4', 'off');
            }
        });

        function toggleLED(led, state) {
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/" + led + "/" + state, true);
            xhttp.send();
        }
    </script>
</body>
</html>
"""

def web_page():
    return html

# Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    led_on = request.find('/1/on')
    led_off = request.find('/1/off')
    if led_on == 6:
        led1.value(0)
    if led_off == 6:
        led1.value(1)

    led_on = request.find('/2/on')
    led_off = request.find('/2/off')
    if led_on == 6:
        led2.value(0)
    if led_off == 6:
        led2.value(1)

    led_on = request.find('/3/on')
    led_off = request.find('/3/off')
    if led_on == 6:
        led3.value(0)
    if led_off == 6:
        led3.value(1)

    led_on = request.find('/4/on')
    led_off = request.find('/4/off')
    if led_on == 6:
        led4.value(0)
    if led_off == 6:
        led4.value()

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
