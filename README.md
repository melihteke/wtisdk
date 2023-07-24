[![PyPI Version](https://img.shields.io/pypi/v/wtisdk.svg)](https://pypi.org/project/wtisdk/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/melihteke/wtisdk/actions/workflows/python-publish.yml)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


![image](https://github.com/melihteke/wtisdk/assets/36086368/24e4279e-54b6-4f3c-8d57-81ce9a005c89)

# WTI SDK - API Wrapper for Western Telematic Inc. (WTI)
WTI SDK is a Python library that serves as an API wrapper for Western Telematic Inc. (WTI) devices. It provides a convenient way to interact with WTI devices and perform various actions.

Please note that WTI is a vendor specializing in console and power management solutions for network equipment. Their devices offer advanced features for managing and controlling network infrastructure.

This SDK, developed by Melih Teke, aims to simplify the integration with WTI devices and enhance the functionality for managing and controlling network infrastructure.

Please refer to the WTI Website for more information about Western Telematic Inc. and their range of devices.

Please note that this SDK is not an official tool provided by Western Telematic Inc., but an independent contribution to facilitate working with their devices.

**Disclaimer: All risks associated with the usage of this SDK are the responsibility of the users. It is recommended to thoroughly test the SDK in a non-production environment before deploying it in a production environment.**

For any questions or support, please contact me at me@mteke.com

## Features
- Connect to WTI devices and retrieve operational data.
- Change configuration.
- Manage the device.

### Installation
```sh
pip install wtisdk
```


### Basic Usage
```sh
(.venv) [mteke@devnet-server test_infra]$ ipython
Python 3.10.8 (default, Aug 13 2020, 07:46:32) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.16.3 -- An enhanced Interactive Python. Type '?' for help.

In [1]: device = { "host": "10.20.30.139",
   ...:            "username": "USERNAME",
   ...:            "password": "PASSWORD"
   ...:           }

In [2]: from wtisdk import WtiClient

In [3]: client = WtiClient(**device)

In [4]: client.get_status()
Out[4]: 
{'status': {'code': '0', 'text': 'OK'},
 'vendor': 'WTI',
 'product': 'CPM-800-2-EA',
 'totalports': '8',
 'totalplugs': '8',
 'softwareversion': '7.04 4 Sep 2022',
 'serialnumber': '01910453453191231',
 'assettag': '153561',
 'siteid': 'DEV6S01',
 'analogmodemphonenumber': '',
 'modeminstalled': 'No',
 'gig_dualphy': 'Yes, Yes',
 'cpu_boardprogramdate': 'ARM, 10-31-2019',
 'ram_flash': '512 MB, 128 MB',
 'lineinputcount_rating': '1 ,  20 Amps',
 'currentmonitor': 'No',
 'keylength': '2048',
 'apacheversion': '2.4.49',
 'bashversion': '5.0.0(1)-release',
 'ipsecversion': '5.9.4/K5.4.0',
 'netsnmpversion': '5.9.1',
 'opensslversion': '1.0.2u-fips  20 Dec 2019',
 'opensshversion': '8.8p1',
 'openvpnversion': '2.5.3',
 'apirelease': 'March 2020',
 'uptime': '903918.86',
 'restful': 'v1.0, v2 (Jan22)',
 'macaddresses': [{'mac': '00-09-9b-01-a7-34'}, {'mac': '00-09-9b-f6-a7-56'}],
 'interface_list': 'eth0, eth1'} 

```

### Retrieving Serial Port Configuration
To retrieve the configuration of the serial ports from the WTI device, use the following method:
```sh
config = client.get_serial_port_config()
```
This method returns a dictionary containing the serial port configuration if the API request is successful. Otherwise, it returns an integer representing the HTTPS status code.

### Retrieving Temperature Status
To retrieve the temperature status from the WTI device, use the following method:
```sh
temperature = client.get_temperature()

{"status": {"code": "0", "text": "OK"},
 "temperature": "35",
 "format": "C",
 "timestamp": "2023-05-27T02:58:28+00:00"}
```

### Retrieving Firmware Status
To retrieve the firmware status from the WTI device, use the following method:
```sh 
firmware_status = client.get_firmware_status()
```

### Retrieving Alarm Status
To retrieve the alarm status from the WTI device, use the following method:
```sh 
alarm_status = client.get_alarm_status()
```

### Editing Power Plug Plugconfig
To edit the power plug configuration on the WTI device using the powerplugconfig endpoint, use the following method:
```sh 
config = {
    "plug": 8,
    "plugname": "Outlet_A1",
    "bootdelay": 0,
    "default": 0,
    "bootpriority": 2
}  # Replace with the desired configuration
response = client.edit_power_plug_plugconfig(config)
```

### Get Specific User
Retrieves information about a specific user from the WTI device.
```sh 
client = WtiClient(host, username, password)
user_info = client.get_specific_user("Melih Teke")
print(user_info)
```
### Add new user
Add a new user using the provided configuration.
```sh 
client = WtiClient(host, username, password)
new_user_config = {
    "users": {
        "username": "new_user",
        "newpasswd": "new_user",
        "accesslevel": 3,
        "portaccess": "11111111111111111111111111111",
        "plugaccess": "11111111111111111111",
        "groupaccess": "111111111111111111111111111111111111111111111111111111",
        "accessserial": 1,
        "accessssh": 1,
        "accessweb": 1,
        "accessoutbound": 1,
        "accessmonitor": 1,
        "callbackphone": "9313233344556"
    }
}
response = client.add_new_user(new_user_config)
```
### Edit User
Edit an existing user using the provided configuration.

```sh 
client = WtiClient(host, username, password)
user_config = {
    "users": {
        "username": "Melih Teke",
        "newpasswd": "new_password",
        "accesslevel": 3,
        "portaccess": "11111111111111111111111111111",
        "plugaccess": "11111111111111111111",
        "groupaccess": "111111111111111111111111111111111111111111111111111111",
        "accessserial": 1,
        "accessssh": 1,
        "accessweb": 1,
        "accessoutbound": 1,
        "accessmonitor": 1,
        "callbackphone": "9313233344556"
    }
}
response = client.edit_user(user_config)
```

### Delete User
Delete an existing user specified by the username.

```sh 
client = WtiClient(host, username, password)
response = client.delete_user("Melih Teke")
```

### Retrieve Serial Port Configuration
Retrieves the configuration of all serial ports from the WTI device.
```sh 
client = WtiClient(host, username, password)
serial_port_config = client.get_all_serial_port_config()
print(serial_port_config)
```
### Retrieve Specific Serial Port Configuration
Retrieves the configuration of a specific serial port from the WTI device.
```sh 
client = WtiClient(host, username, password)
specific_port_config = client.get_specific_serial_port_config("COM1")
print(specific_port_config)
```

### Retrieve AAA Server configuration
Retrieve the configuration of a WTI AAA server.

```sh
client = WtiClient(host, username, password)
aaa_server_config = client.get_aaa_server_config('tacacs')
print(aaa_server_config)
```

### Network Interface Configuration
Retrieves the configuration of a network interface.
```sh
client = WtiClient(host, username, password)
interface_config_all = client.get_network_interface_config()
print(interface_config_all)

interface_config_eth0 = client.get_network_interface_config('eth0')
print(interface_config_eth0)

```

### Edit Network Interface Configuration
Edits the configuration of a network interface.

```sh 
client = WtiClient(host, username, password)
new_interface_config = {
    "interface": {
        "name": "eth0",
        "ietf-ipv4": {
            "address": [
                {
                    "ip": "10.60.11.101",
                    "netmask": "255.255.255.240",
                    "gateway": "10.20.11.97"
                }
            ]
        }
    }
}
updated_config = client.edit_network_interface_config(new_interface_config)
print(updated_config)
```

### Retrieve Hostname and location of the device
```sh 
client = WtiClient(host, username, password)
hostname_config = client.get_config_hostname()
print(hostname_config)
```

### Edit hostname of the device
Edits the hostname configuration of the device.

```sh 
{
    "unitid": {
        "hostname": "DSMLABIRVINE",
        "location": "RACK12IRVINE",
        "assettag": "1028561"
    }
}

client = WtiClient(host, username, password)
new_hostname_config = {
    "unitid": {
        "hostname": "DSMLABIRVINE",
        "location": "RACK12IRVINE",
        "assettag": "1028561"
    }
}
updated_hostname_config = client.edit_config_hostname(new_hostname_config)
print(updated_hostname_config)

```

### Retrieve Timedate
Retrieves the current time and date configuration of the device.
```sh 
client = WtiClient(host, username, password)
timedate_config = client.get_config_timedate()
print(timedate_config)
```

### Edit Timedate
Edits the time and date configuration of the device.
```sh 
config = {
    "date": "05/25/2023",
    "time": "18:52:00",
    "timezone": 5,
    "ntp": {
        "enable": 0,
        "ietf-ipv4": {
            "address": [
                {
                    "primary": "100.197.181.20",
                    "secondary": "100.197.181.12"
                }
            ]
        },
        "ietf-ipv6": {
            "address": [
                {
                    "primary": "",
                    "secondary": ""
                }
            ]
        },
        "timeout": 6
    }
}

client = WtiClient(host, username, password)
new_timedate_config = {
    "date": "05/25/2023",
    "time": "18:52:00",
    "timezone": 5,
    "ntp": {
        "enable": 0,
        "ietf-ipv4": {
            "address": [
                {
                    "primary": "100.197.181.20",
                    "secondary": "100.197.181.12"
                }
            ]
        },
        "ietf-ipv6": {
            "address": [
                {
                    "primary": "",
                    "secondary": ""
                }
            ]
        },
        "timeout": 6
    }
}
updated_timedate_config = client.edit_config_timedate(new_timedate_config)
print(updated_timedate_config)

```

### Retreive Web Service configuration
Retrieves the configuration of the device's web service.

```sh
client = WtiClient(host, username, password)
web_service_config = client.get_config_web_service()
print(web_service_config)
```

### Retreive SNMP TRAP
Retrieves the SNMP trap configuration.
```sh 
client = WtiClient(host, username, password)
snmp_trap_config = client.get_config_snmp_trap()
print(snmp_trap_config)
```

### Edit SNMP TRAP
Modifies the SNMP trap configuration.

```sh 
config = {
    "snmptraps": {
        "ietf-ipv4": {
            "clear": 0,
            "community": "community",
            "version": 2,
            "trapengineidv3": "",
            "managers": [
                {
                    "manager": "manag1",
                    "index": "1"
                },
                {
                    "manager": "manag3",
                    "index": "3"
                }
            ]
        }
    }
}
```

```sh 
client = WtiClient(host, username, password)
new_snmp_trap_config = {
    "snmptraps": {
        "ietf-ipv4": {
            "clear": 0,
            "community": "community",
            "version": 2,
            "trapengineidv3": "",
            "managers": [
                {
                    "manager": "manag1",
                    "index": "1"
                },
                {
                    "manager": "manag3",
                    "index": "3"
                }
            ]
        }
    }
}
updated_snmp_trap_config = client.edit_config_snmp_trap(new_snmp_trap_config)
print(updated_snmp_trap_config)
```

### Retrieve SNMP Access Configuration
Retrieves the SNMP access configuration from the device.

```sh 
client = WtiClient(host, username, password)
snmp_access_config = client.get_config_snmp_access()
print(snmp_access_config)
```

### Edit SNMP Access Configuration
Edits the SNMP access configuration on the device.

```sh 
config = {
    "snmpaccess": [
        {
            "eth0": [
                {
                    "ietf-ipv4": {
                        "enable": 0,
                        "version": 2,
                        "readonly": 0,
                        "systemname": "",
                        "contact": "",
                        "location": "",
                        "rocommunity": "public",
                        "rwcommunity": "public",
                        "users": [
                            {
                                "username": "fgffgfg",
                                "authpriv": "1",
                                "authpass": "sdsdsdsd",
                                "authproto": "0",
                                "privpass": "",
                                "privproto": "0",
                                "index": "1"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}

```

```sh 
client = WtiClient(host, username, password)
new_snmp_access_config = {
    "snmpaccess": [
        {
            "eth0": [
                {
                    "ietf-ipv4": {
                        "enable": 0,
                        "version": 2,
                        "readonly": 0,
                        "systemname": "",
                        "contact": "",
                        "location": "",
                        "rocommunity": "public",
                        "rwcommunity": "public",
                        "users": [
                            {
                                "username": "fgffgfg",
                                "authpriv": "1",
                                "authpass": "sdsdsdsd",
                                "authproto": "0",
                                "privpass": "",
                                "privproto": "0",
                                "index": "1"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
updated_snmp_access_config = client.edit_config_snmp_access(new_snmp_access_config)
print(updated_snmp_access_config)

```

### Retrieve IP Tables
Retrieves the IP tables configuration from the device.

```sh 
client = WtiClient(host, username, password)
ip_tables_config = client.get_config_ip_tables()
print(ip_tables_config)

```


### Edit IP Tables
Edits the IP tables configuration on the device.
```sh 
config = {
    "iptables": {
        "eth0": {
            "ietf-ipv4": {
                "clear": 1,
                "entries": [
                    {
                        "entry": "iptables -A INPUT -i lo -j ACCEPT",
                        "index": "1"
                    }
                ]
            }
        }
    }
}

```

```sh 
client = WtiClient(host, username, password)
new_ip_tables_config = {
    "iptables": {
        "eth0": {
            "ietf-ipv4": {
                "clear": 1,
                "entries": [
                    {
                        "entry": "iptables -A INPUT -i lo -j ACCEPT",
                        "index": "1"
                    }
                ]
            }
        }
    }
}
updated_ip_tables_config = client.edit_config_ip_tables(new_ip_tables_config)
print(updated_ip_tables_config)

```

### Retrieve Syslog Server configuration
Retrieves the configuration of the syslog server from the device.

```sh 
client = WtiClient(host, username, password)
syslog_server_config = client.get_config_syslog_server()
print(syslog_server_config)
```

### Edit Syslog Server configuration
Edits the configuration of the syslog server on the device.
```sh 
config = {
    "syslogserver": {
        "eth0": [
            {
                "ietf-ipv4": {
                    "enable": 0,
                    "port": "514",
                    "transport": "0",
                    "secure": "0",
                    "block": [
                        {
                            "address": "",
                            "index": "1"
                        }
                    ]
                }
            }
        ]
    }
}
```

```sh 
client = WtiClient(host, username, password)
new_syslog_server_config = {
    "syslogserver": {
        "eth0": [
            {
                "ietf-ipv4": {
                    "enable": 0,
                    "port": "514",
                    "transport": "0",
                    "secure": "0",
                    "block": [
                        {
                            "address": "",
                            "index": "1"
                        }
                    ]
                }
            }
        ]
    }
}
updated_syslog_server_config = client.edit_config_syslog_server(new_syslog_server_config)
print(updated_syslog_server_config)
```

### Retrieve Syslog client configuration
Retrieves the configuration of the syslog client from the device.

```sh 
client = WtiClient(host, username, password)
syslog_client_config = client.get_config_syslog_client()
print(syslog_client_config)
```


### Edit Syslog client configuration
Edits the configuration of the syslog client on the device.

```sh 
config = {
    "syslogclient": {
        "ietf-ipv4": {
            "clear": "0",
            "clients": [
                {
                    "address": "9.9.9.1",
                    "port": "504",
                    "transport": "0",
                    "secure": "0",
                    "cert": "",
                    "index": "1"
                }
            ]
        }
    }
}

```

```sh 
client = WtiClient(host, username, password)
new_syslog_client_config = {
    "syslogclient": {
        "ietf-ipv4": {
            "clear": "0",
            "clients": [
                {
                    "address": "9.9.9.1",
                    "port": "504",
                    "transport": "0",
                    "secure": "0",
                    "cert": "",
                    "index": "1"
                }
            ]
        }
    }
}
updated_syslog_client_config = client.edit_config_syslog_client(new_syslog_client_config)
print(updated_syslog_client_config)

```




## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Resources
- [WTI Website](https://www.wti.com/)
- [WTI API Documentation](https://ftp.wti.com/pub/TechSupport/Restful_WTI/current/api/api.html#)

## Acknowledgments
The dnacsdk library served as an inspiration while I started to write this library.

## Credits
The WTI SDK is maintained by Melih Teke. This is not an official tool provided by Western Telematic Inc. !




