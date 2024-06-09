import network

def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        pass
    
    print('network config:', wlan.ifconfig())
    return wlan



def get_signal_strength(wlan):
    return wlan.status('rssi')



import socket

# Replace with your WiFi credentials
SSID = 'COCO_4g'
PASSWORD = 'coco9213'

wlan = connect(SSID, PASSWORD)




def web_page():
    html = """<!DOCTYPE html>
<html>
<head>
<title>WiFi Signal Strength</title>
</head>
<body>
<h1>WiFi Signal Strength</h1>
<p>Signal strength: <span id="rssi">...</span> dBm</p>
<script>
function updateSignalStrength() {
    fetch('/rssi').then(response => response.text()).then(data => {
        document.getElementById('rssi').innerText = data;
    });
}
setInterval(updateSignalStrength, 1000);
updateSignalStrength();  // Initial call to populate immediately
</script>
</body>
</html>"""
    return html

# Set up the web server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(5)

print('Listening on', addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024).decode()
    print('Request:', request)
    
    if 'GET /rssi' in request:
        rssi = get_signal_strength(wlan)
        response = str(rssi)
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Content-Type: text/plain\r\n')
        cl.send('Connection: close\r\n\r\n')
        cl.sendall(response.encode())
    else:
        response = web_page()
        cl.send('HTTP/1.1 200 OK\r\n')
        cl.send('Content-Type: text/html\r\n')
        cl.send('Connection: close\r\n\r\n')
        cl.sendall(response.encode())
    
    cl.close()


