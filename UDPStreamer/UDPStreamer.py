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
    l_time = ac.getCarState(0, acsys.CS.LapTime)
    l_pos = ac.getCarState(0, acsys.CS.NormalizedSplinePosition)
    l_Ltime = ac.getCarState(0, acsys.CS.LastLap)
    

    #f_time = "{}:{}.{:02}".format(l_time // 60000, (l_time % 60000) // 1000, l_time % 1000)
    #f_Ltime = "{}:{}.{:02}".format(l_Ltime // 60000, (l_Ltime % 60000) // 1000, l_Ltime % 1000)


    # Format message: "Speed|RPM|Gear"
    message = "{:.0f}|{:.0f}|{:.0f}|{}|{:.3f}|{}".format(l_speed, l_rpm, l_gear, l_time, l_pos, l_Ltime)
    
    try:
        sock.sendto(bytes(message, "utf-8"), (UDP_IP, UDP_PORT))
    except Exception as e:
        pass # Avoid crashing the UI if network fails