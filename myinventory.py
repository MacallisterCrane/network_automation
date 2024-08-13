#!/usr/bin/python3
import configparser
config = configparser.ConfigParser()
config['Switches'] = {}
switches = config['Switches']
switches['hostname1'] = 'Local_Switch'
switches['hostname2'] = 'IT_Network'
switches['hostname3'] = 'MGMT_Network'
switches['hostname4'] = 'ACCT_Network'
config['[Switches:vars]'] = {}
switchvars['RAM'] = '512MB'
switchvars['vCPU'] = '1'
switchvars['RAM'] = '/usr/bin/qemu-system-x86_64(v4.2.1)'
switchvars['RAM'] = 'CD/DVD-ROM or HDD'
switchvars['RAM'] = 'Power off the VM'
switchvars['RAM'] = 'telnet'
switchvars['RAM'] = '13'
switchvars['RAM'] = 'realtek 8139 ethernet (rtl8139)'
switchvars['RAM'] = 'on'
switchvars['RAM'] = '0c:1c:b2:85:00:00'
switchvars['RAM'] = '0c:cc:78:5d:00:00'
switchvars['RAM'] = '0c:40:34:07:00:00'
switchvars['RAM'] = '0c:e0:f2:0b:00:00'
switchvars['RAM'] = '0c:c0:5e:66:00:00'
with open('newinventory.ini', 'w') as configfile:
        config.write(configfile)