#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address For" + interface + "to" + new_mac)
    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "to" , new_mac])
    subprocess.call(["ifconfig" , interface , "up"])


parser = optparse.OptionParser()

#Interface/MAC Address
parser.add_option("-i, --interface", dest ="interface", help="Interface To Change It's MAC Address")
parser.add_option("-m, --mac", dest ="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

change_mac(options.interface, options.new_mac)
