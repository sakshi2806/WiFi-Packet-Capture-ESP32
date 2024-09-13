import pyshark

# Read the PCAP file
capture = pyshark.FileCapture('capture1.pcap')

# Iterate over the packets
for packet in capture:
    # Print the packet summary
    print(packet)
    
    # Print the packet details
    packet.show()
