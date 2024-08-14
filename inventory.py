from netmiko import ConnectHandler

# List of switches with their connection details
switches = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret'
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.2.1',
        'username': 'admin',
        'password': 'password',
        'secret': 'secret'
    }
]

inventory = []

for switch in switches:
    connection = ConnectHandler(**switch)
    connection.enable()  # Enter enable mode if required
    general_settings = connection.send_command("show running-config")
    network_settings = connection.send_command("show ip interface brief")
    inventory.append({
        'General Settings': general_settings,
        'Network Settings': network_settings
    })
    connection.disconnect()

with open('inventory.txt', 'w') as file:
    for item in inventory:
        file.write(f"{item}\n")

print("Inventory file created.")