
import time
import json
import serial

# SERIAL PORT CONFIG
# Adjust based on your platform and Arduino setup
SERIAL_PORT = "/dev/ttyUSB0"  # Example: COM3 on Windows, /dev/ttyUSB0 on Linux
BAUD_RATE = 9600

# Load gesture mappings (servo angles, LED patterns)
def load_gestures(path="body/gestures.json"):
    with open(path, "r") as f:
        return json.load(f)

# Send a command to the Arduino
def send_gesture(command):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
            time.sleep(1)  # wait for connection to settle
            ser.write((command + "\n").encode())
            print(f"[Servo/LED] Sent: {command}")
    except Exception as e:
        print(f"[Error] Could not send gesture: {e}")

# Trigger a ritual-based body gesture
def perform_ritual_motion(ritual_name):
    gestures = load_gestures()
    if ritual_name in gestures:
        for action in gestures[ritual_name]:
            send_gesture(action)
            time.sleep(0.5)
    else:
        print(f"[Warning] Unknown ritual: {ritual_name}")
