import subprocess

# Define the output file name
output_file = 'wifi_list.txt'

# Run the iwlist command to scan for available wireless networks
scan_output = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8')

# Create an empty set to store unique network entries
networks = set()

# Parse the output and extract SSID and encryption type for each network
for line in scan_output.split('\n'):
    if 'ESSID:' in line:
        ssid = line.split(':')[1].strip().strip('"')
    elif 'Encryption key:' in line:
        encryption = 'Open' if 'off' in line else 'WEP/WPA/WPA2'
        networks.add((ssid, encryption))

# Write the unique network entries to the output file
with open(output_file, 'w') as f:
    for ssid, encryption in networks:
        f.write('{}\t{}\n'.format(ssid, encryption))
