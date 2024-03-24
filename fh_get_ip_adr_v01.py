#FIND IP ADDRESS FOR Futurehome HUB
#For Python3

#Run the program from a Raspberrry Pi
#with Raspberry Pi in the same local network as Futurehome HUB

#If your local router use DHCP to set ip address for the Futurehome HUB
#this program may help you to find the ip address
#In this example local ip segement is 192.168.1.x
#You have to install nmap and netcat

import os

# List IP adresses for all units on local network to file
cmd = "nmap -sP 192.168.1.0/24 > fh_ip_network.out"  # Save result in file
os.system(cmd)

# Read result file lines
local_ip_adr_file = open('fh_ip_network.out', 'r')
Lines = local_ip_adr_file.readlines()

# Convert file lines to list
list_of_ip_adr = []
for line in Lines:
    ip_adr_line = line
    length_ip_adr_line = len(ip_adr_line)
    nmap_scan = line[0:9]
    #Test content of line for text "Nmap scan", if yes save ip address in list
    if nmap_scan == "Nmap scan":
        ip_adr = line[21:]
        stripped_ip_adr = ip_adr.strip()  #Remove /n
        list_of_ip_adr.append(stripped_ip_adr)

# Ping a spesific ip address and port with netcat
for ip_address in list_of_ip_adr:
    cmd = "nc -vv -z " + ip_address + " 1884 > fh_nc_result.out 2>&1"
    os.system(cmd)

    # Read result file line
    nc_res_file = open('fh_nc_result.out', 'r')
    nc_result = nc_res_file.readline()

    # Test content of line for text "succeeded!", if yes the Future Hub ip address is found
    if "succeeded!" in nc_result:
        futurehome_ip_adr = ip_address
        print("Futurehome IP address: ",futurehome_ip_adr)

        # Save ip address in file
        output_file = "fh_ip_adr.txt"
        with open(output_file, "w") as data_file:
            data_file.write(futurehome_ip_adr)
