import socket
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

# This function runs in the background to listen for UDP packets
def udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 5005))
    
    while True:
        data, addr = sock.recvfrom(1024)
        raw_string = data.decode()
        
        # 1. Split the string into a list
        # Example input: "240,7500,4,95"
        parts = raw_string.split('|') 
        
        # 2. Package it into a Dictionary (JSON)
        telemetry = {
            "speed": parts[0],
            "rpm": parts[1],
            "gear": parts[2],
        }
        # print(telemetry)
        
        # 3. Send the whole object to the dashboard
        socketio.emit('new_data', {'raw': telemetry})
        
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=udp_listener, daemon=True).start()
    socketio.run(app, debug=True, use_reloader=False)