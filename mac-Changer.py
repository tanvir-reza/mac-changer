#!/usr/bin/env python

import subprocess


print(" Chose Your Interface")
print("     eth0 ")
print("     wlan0")

interface = raw_input("Enter your Choice : ")

mac_address = raw_input("Enter Your New Mac Address -> ")

print("[+] Mac address change From " + interface + " and Mac address is " + mac_address)

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["sudo", "ifconfig", interface, "up"])


print(" Mac Change SuccessFully !!!! ")