import serial
import time

#grabbing port from usb
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

change = input("Is the port different? ")

if change.lower() == 'n' or (change[0].lower() == 'n' and change[1] == 'o'):
    port = 1101
else:
    port = input("Enter the numerical portion of the port: ")
age = int(input("How old are you? "))
arduino = serial.Serial(f"/dev/cu.usbmodem{port}", 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

print("Reading BPM data...")

while True:
    if arduino.in_waiting > 0:
        bpm = arduino.readline().decode('utf-8').strip()
        if bpm.isdigit():
            if 140<= int(bpm) <= 220 - age:
                print(f"BPM: {RED}{bpm}{RESET}")
            elif 100 <= int(bpm) < 140:
                print(f"BPM: {YELLOW}{bpm}{RESET}")
            else:
                print(f"BPM: {GREEN}{bpm}{RESET}")

