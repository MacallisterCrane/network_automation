#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass

if __name__ == "__main__":
	device_dict = {
#device_type, IP, and username can be replaced with any type of device        
		"device_type" : "extreme_exos",
		"host" : "10.10.1.24",
		"username" : "admin",
		"password" : getpass(),
	}
	
	netmiko_device = ConnectHandler(**device_dict)
	print(netmiko_device.find_prompt())
	print(
#Line 17 command can be replaced or expanded upon with any command for the device type 
		netmiko_device.send_command("configure vlan localvlan tag 100")
	)
	print(dir(netmiko_device))
	netmiko_device.disconnect()