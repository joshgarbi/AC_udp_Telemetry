import ac
import acsys
import socket

# Configuration
UDP_IP = "127.0.0.1" # Change to remote IP if needed
UDP_PORT = 5005

# Initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def acMain(ac_version):
    app_name = "UDP Streamer"
    app = ac.newApp(app_name)
    ac.setSize(app, 200, 50)
    
    ac.log("UDP Streamer loaded")
    return app_name

def acUpdate(delta_t):
    # Get Data
    l_speed = ac.getCarState(0, acsys.CS.SpeedKMH)
    l_rpm = ac.getCarState(0, acsys.CS.RPM)
    l_gear = ac.getCarState(0, acsys.CS.Gear)

    # Format message: "Speed|RPM|Gear"
    message = "{:.0f}|{:.0f}|{}".format(l_speed, l_rpm, l_gear)
    
    try:
        sock.sendto(bytes(message, "utf-8"), (UDP_IP, UDP_PORT))
    except Exception as e:
        pass # Avoid crashing the UI if network fails