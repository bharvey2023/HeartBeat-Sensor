import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

def makeprofile(old,data):
    mycursor = None
    mydb = None
    try:
        # 1. Establish database connection
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="heartbeat"
        )

        # 2. Create a cursor object
        mycursor = mydb.cursor()
        name = input("Whats your name? ")
        weight = int(input("How much do you weigh: "))
        height =int(input("Height in inches: "))
        choice = input("Want to add a number and email: ")
        # 3. Prepare the INSERT statement with placeholders
        if choice.lower() == "yes":
            email = input("email: ")
            if "@" not in email:
                while "@" not in email:
                    email = input("email with @: ")
            num = input("phone number: ")
            sql = "INSERT INTO user (username,email,age,phonenumber,weight,height_in,avg_hb,med_hb) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (name, email, old, num, weight, height, np.mean(data), np.median(data))
        else:
            sql = "INSERT INTO user (username,age,weight,height_in,avg_hb,med_hb) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (name, old, weight, height, np.mean(data), np.median(data))
        # 4. Execute the INSERT statement
        mycursor.execute(sql, val)

        # 5. Commit the changes
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # 6. Close the cursor and connection
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydb' in locals() and mydb.is_connected():
            mydb.close()

#printing statistics of the data
def printstats(data):
    print(f"Non sorted: {data}")
    sorted_bpm = np.sort(data)
    print(f"Sorted: {sorted_bpm}")
    mean_bpm = float(np.mean(data))
    median_bpm = float(np.median(data))
    print(f"Average BPM: {mean_bpm}")
    print(f"Median BPM: {median_bpm}")

#reading the beats per minute
def read_bpm(board,old,ran):
    data = np.empty(0)
    while len(data) < ran:
        if board.in_waiting > 0:
            bpm = board.readline().decode('utf-8').strip()
            if bpm.isdigit() and 50 <= int(bpm) <= (220 - old) - 20:
                data = np.append(data, int(bpm))
    return data

#plotting data on a graph
def plot(data,ran):
    x = np.arange(1, ran+1)
    plt.figure(figsize=(5, 4))
    #plt.plot(x,data,linewidth=3,color='red')
    plt.scatter(x, data, s=115, c=data, cmap='RdYlGn_r')
    plt.ylabel('Beats per Minute', fontsize=14)
    plt.xlabel('Interval/seconds', fontsize=14)
    plt.colorbar(label='Range')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

#grabbing port from usb
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
bpm_data = np.empty(0)
#print(bpm_data)
r = 0

change = input("Is the port different? ")

if change.lower() == "no":
    port = 101
else:
    port = input("Enter the numerical portion of the port: ")


age = int(input("How old are you? "))
arduino = serial.Serial(f"/dev/cu.usbmodem{port}", 9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

change = "yes"
while change.lower() == "yes":
    r = int(input("How many iterations? Options are 5 10 15 20 25: "))
    while r % 5 !=0 or r > 25:
        r = int(input("Options are 5 10 15 20 25: "))
    print("Reading BPM data...")

    bpm_data = read_bpm(arduino, age,r)
    printstats(bpm_data)

    change = input("Wanna try again? ")

change = input("Do you want to graph the data?")

if change.lower() == "yes":
    plot(bpm_data,r)

change = input("Do you want to make a profile?")

if change.lower() == "yes":
    makeprofile(age,bpm_data)
