#!/usr/local/bin/python
# Netmiko Python Module Library Template for NXOS

# Importing necessary modules
import netmiko
from netmiko import ConnectHandler

# Creating the Netmiko class based network device dictionary
switch = {
'device_type': 'cisco_nxos',
'ip': '<ip address>',
'username': '<username>',
'password': '<password>',
'port' : 22,
'verbose': True,
}

# SSH connection using Connection handler device dictionary
net_connect = ConnectHandler(**switch)
net_connect.find_prompt()

# Configuration commands
config_commands = [ '<config command 1>',
                    '<config command 2>',
                    '<config command 3>' ]


# Send commands to switch through interactive SSH 'shell'
output = net_connect.send_config_set(config_commands)

# Print output to screen
print(output)

# Disconnect SSH session
net_connect.Disconnect()
