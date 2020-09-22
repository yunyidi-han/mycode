#!/usr/bin/env python3
from ipaddress import ip_address
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

try: 
    ipchk = str(ip_address(ipchk))
    # if user set IP of gateway
    if ipchk == "192.168.70.1":
       print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk: # if any data is provided, this will test true
       print("Looks like the IP address was set: " + ipchk) # indented under if
except ValueError:
    print("You did not provide a valid IPv4 input.") # indented under else

