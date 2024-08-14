from netmiko import ConnectHandler

# List of switches with their connection details
switches = [
    {
        'device_type': 'extreme_exos',
        'host': '10.10.1.24',
        'username': 'admin',
        'password': '',
    }
]

inventory = []

for switch in switches:
    connection = ConnectHandler(**switch)
    connection.enable()  # Enter enable mode if required
    general_settings = connection.send_command("show config")
    network_settings = connection.send_command("show ipconfig")
    inventory.append({
        'General Settings': general_settings,
        'Network Settings': network_settings
    })
    connection.disconnect()

with open('inventory.txt', 'w') as file:
    for item in inventory:
        file.write(f"{item}\n")

print("Inventory file created.")
