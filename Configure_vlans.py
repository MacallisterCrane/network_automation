#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass

if __name__ == "__main__":
	device_dict = {
#device_type, IP, and username can be replaced with any type of device        
		"device_type" : "extreme_exos",
		"host" : "10.10.1.X",
		"username" : "admin",
		"password" : getpass(),
	}
	
	netmiko_device = ConnectHandler(**device_dict)
	print(netmiko_device.find_prompt())
	print(
#Line 18 command can be replaced or expanded upon with any command for the device type 
		netmiko_device.send_command("configure vlan <name> tag <#>")
	)
	print(dir(netmiko_device))
	netmiko_device.disconnect()