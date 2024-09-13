import serial
import io
import os
import subprocess
import signal
import time

import pyshark

try:
    serialportInput = input("[?] Select a serial port (default '/dev/COM3'): ")
    if serialportInput == "":
        serialport = "COM3"
    else:
        serialport = serialportInput
except KeyboardInterrupt:
    print("\n[+] Exiting...")
    exit()

try:
    canBreak = False
    while not canBreak:
        boardRateInput = input("[?] Select a baudrate (default '115200'): ")
        if boardRateInput == "":
            boardRate = 115200
            canBreak = True
        else:
            try:
                boardRate = int(boardRateInput)
            except KeyboardInterrupt:
                print("\n[+] Exiting...")
                exit()
            except Exception as e:
                print("[!] Please enter a number!")
                continue
            canBreak = True
except KeyboardInterrupt:
    print("\n[+] Exiting...")
    exit()

try:
    filenameInput = input("[?] Select a filename (default 'capture.pcap'): ")
    if filenameInput == "":
        filename = "capture.pcap"
    else:
        filename = filenameInput
except KeyboardInterrupt:
    print("\n[+] Exiting...")
    exit()

canBreak = False
while not canBreak:
    try:
        ser = serial.Serial(serialport, boardRate)
        canBreak = True
    except KeyboardInterrupt:
        print("\n[+] Exiting...")
        exit()
    except:
        print("[!] Serial connection failed... Retrying...")
        time.sleep(2)
        continue

print("[+] Serial connected. Name: " + ser.name)
counter = 0
f = open(filename,'wb') #The wb indicates that the file is opened for writing in binary mode

check = 0
while check == 0:
    print(check)
    line = ser.readline()
    print(check)
    if b"<<START>>" in line:
      check = 1
    print(check)
    
    print("[+] Stream started...")
   




from scapy.all import *

pkts = []                      
pname="captures.pcap"
try:
    while True:
        ch = ser.readline()
        pkts.append(ch)
        wrpcap(pname, pkts)
        pkts.clear()
        a=rdpcap("captures1.pcap")
        print(a)
        

        f.write(ch)
        f.flush()
except KeyboardInterrupt:
    print("[+] Stopping...")
    

f.close()
ser.close()
print("[+] Done.")


