#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def main():
    try:
        inter = input("What interface do you want to find info on? ")
        meth = input("Do you want the MAC or the IP? ").lower()
        if meth == "ip":
            ip(inter)
        elif meth == "mac":
            mac(inter)

    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

def ip(adpt):
    print('\n****** details of interface - ' + adpt + ' ******')
    print('IP: ', end='')  # This print statement will always print IP without an end of line
    print((netifaces.ifaddresses(adpt)[netifaces.AF_INET])[0]['addr']) # Prints the IP address

def mac(adpt):
    print('\n****** details of interface - ' + adpt + ' ******')
    print('MAC: ', end='') # This print statement will always print MAC without an end of line
    print((netifaces.ifaddresses(adpt)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address

main()
