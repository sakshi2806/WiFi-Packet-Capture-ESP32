# WiFi Packet Sniffer

This project demonstrates a WiFi packet sniffer using an ESP32, capable of capturing and storing WiFi packets in a PCAP file format. The captured packets can be analyzed using standard tools like Wireshark.

## Table of Contents

- [Overview](#overview)
- [Components Used](#components-used)
- [ESP32 Code](#esp32-code)
  - [Settings](#settings)
  - [Setup](#setup)
  - [Channel Hopping](#channel-hopping)
  - [Packet Sniffer Function](#packet-sniffer-function)
- [Python Scripts](#python-scripts)
  - [Serial Data Capture](#serial-data-capture)
  - [Read PCAP File](#read-pcap-file)
- [Usage Instructions](#usage-instructions)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Overview

This project involves an ESP32 configured to operate as a WiFi packet sniffer. The captured packets are sent over serial to a PC where they are saved in a PCAP file format using Python scripts.

## Components Used

- **ESP32**: Acts as the WiFi packet sniffer.
- **Serial Monitor**: Used to read the captured packets from the ESP32.
- **Python**: Used for capturing serial data and processing PCAP files.

## ESP32 Code

The ESP32 code is designed to operate with PlatformIO in Visual Studio Code. Below is a brief overview of the code and its functionality.

### Settings

```cpp
#define CHANNEL 1
#define BAUD_RATE 115200
#define CHANNEL_HOPPING true // Scan on all channels
#define MAX_CHANNEL 11
#define HOP_INTERVAL 214 // Channel hopping interval in ms
```

### Setup
1. **Serial Initialization:** Sets up serial communication for debugging and packet output.
2. **WiFi Configuration:** Initializes WiFi in promiscuous mode to capture packets.
3. **Promiscuous Mode:** Sets the ESP32 to promiscuous mode to intercept all WiFi packets on the specified channel.

### Channel Hopping
If `CHANNEL_HOPPING` is enabled, the ESP32 will cycle through all available channels. This allows for a more comprehensive capture of WiFi traffic.

### Packet Sniffer Function
```cpp
void sniffer(void *buf, wifi_promiscuous_pkt_type_t type) {
  wifi_promiscuous_pkt_t* pkt = (wifi_promiscuous_pkt_t*)buf;
  wifi_pkt_rx_ctrl_t ctrl = (wifi_pkt_rx_ctrl_t)pkt->rx_ctrl;

  uint32_t timestamp = now(); // Current timestamp
  uint32_t microseconds = (unsigned int)(micros() - millis() * 1000); // Microseconds offset

  pcap.newPacketSerial(timestamp, microseconds, ctrl.sig_len, pkt->payload); // Send packet via Serial
}
```
The `sniffer` function processes each packet received and sends it to the PCAP class for handling.

## Python Scripts
#### Serial Data Capture

This script is responsible for reading the serial data from the ESP32 and saving it to a PCAP file. It allows you to specify the serial port, baud rate, and output file name. The script captures packets as they are sent from the ESP32 and writes them to the specified PCAP file for later analysis.

#### Read PCAP File
This script reads the captured PCAP file using the `pyshark` library, which is a wrapper around the Wireshark's `tshark`. It allows you to analyze and display the details of the captured packets, helping in understanding the network traffic and diagnosing issues.


## Usage Instructions

1. **PlatformIO Setup**:
   - Open the project in Visual Studio Code with PlatformIO.
   - Ensure all necessary libraries are included in the `platformio.ini` file.

2. **Upload ESP32 Code**:
   - Connect the ESP32 to your computer.
   - Use PlatformIO to upload the provided ESP32 code to the ESP32.

3. **Run Python Scripts**:
   - Connect the ESP32 to your PC via a serial connection.
   - Run the `serial_data_capture.py` script to start capturing packets.
   - Use the `read_pcap_file.py` script to analyze the captured packets.

4. **Monitor Data**:
   - Check the terminal for packet capture status and ensure the capture is ongoing.
   - Review the PCAP file using tools like Wireshark to analyze the captured packets.

## Troubleshooting

1. **Serial Connection Issues**:
   - **Check Port and Baud Rate**: Ensure the correct serial port and baud rate are selected.
   - **Reboot Devices**: Restart the ESP32 and PC if connection issues persist.

2. **Packet Capture Issues**:
   - **Check ESP32 Configuration**: Ensure that the ESP32 is correctly configured to capture packets.
   - **Inspect Serial Output**: Verify that the data is being correctly written to the PCAP file.

3. **PCAP File Analysis**:
   - **Verify PCAP File**: Ensure that the PCAP file is correctly written and not empty.
   - **Use Compatible Tools**: Use tools like Wireshark to read and analyze the PCAP file.

4. **Python Script Errors**:
   - **Library Installation**: Ensure that all required Python libraries (`pyshark`, `serial`, etc.) are installed.
   - **Script Errors**: Check for any errors in the Python script and ensure it matches the expected data format.

## Author 
Sakshi Mishra