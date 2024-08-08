#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass
if __name__ == "__main__":
	device_dict = {
		"device_type" : "extreme_exos",
		"host" : "exos",
		"username" : "admin",
		"password" : getpass(),
	}
	netmiko_device = ConnectHandler(**device_dict)
	print(netmiko_device.find_prompt())
	print(
		netmiko_device.send_command("show vlan")
	)
	print(dir(netmiko_device)
	netmiko_device.disconnect()
