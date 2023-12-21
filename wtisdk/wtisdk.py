import requests
import urllib3

class WtiClient:
    urllib3.disable_warnings()
    
    def __init__(self, host, username, password):
        """
        Initializes a new instance of the WtiClient class.

        Args:
            host (str): The hostname or address of the WTI device.

        """
        self.base_url = "https://" + host
        self.username = username
        self.password = password
        
    def get_status(self):
        """
        Initializes a new instance of the WtiClient class.

        Args:
            host (str): The hostname or address of the WTI device.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        url = f"{self.base_url}/api/v2/status"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_serial_port_config(self):
        """
        Retrieves the configuration of the serial ports from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the serial port configuration.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/serialports"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_temperature(self):
        """
        Retrieves the temperature status from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the temperature status.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/status/temperature"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_firmware_status(self):
        """
        Retrieves the firmware status from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the firmware status.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/status/firmware"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_alarm_status(self):
        """
        Retrieves the alarm status from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the alarm status.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/status/alarms"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_power_plug_config(self):
        """
        Retrieves the power plug configuration from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the power plug configuration.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/powerplug"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_specific_power_plug_config(self,plug_number):
        """
        Retrieves the configuration of a specific power plug from the WTI device.

        Args:
            plug_number (str): The number of the power plug to retrieve the configuration for.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the power plug configuration.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/powerplug?plug=" + plug_number
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code


    def edit_power_plug_config(self, config):
        """
        Edits the power plug configuration on the WTI device.

        Args:
            config (dict, optional): A dictionary containing the power plug configuration to be applied.
                If not provided, the default configuration is used.
                state options: boot, on, off
                
                {
                "plug": 1,
                "plugname": "Outlet_A1",
                "state": "boot"
                }

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the response of the configuration edit.
                If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/powerplug"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def edit_power_plug_plugconfig(self, config):
            """
            Edits the power plug configuration on the WTI device.

            Args:
                config (dict, optional): A dictionary containing the power plug configuration to be applied.
                    If not provided, the default configuration is used.
                    state options: boot, on, off
                    
                    {
                    "plug": 8,
                    "plugname": "Outlet_A1",
                    "bootdelay": 0,
                    "default": 0,
                    "bootpriority": 2
                    }


            Returns:
                dict or int: If the API request is successful, returns a dictionary containing the response of the configuration edit.
                    If an error occurs during the API request, returns an integer representing the HTTP status code.

            """
            url = f"{self.base_url}/api/v2/config/powerplugconfig"
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code
            
    def get_power_config(self):
        """
        Retrieves the power configuration from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the power configuration.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/power"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_specific_user(self, user):
        """
        Retrieves information about a specific user from the WTI device.

        Args:
            user (str): The username of the user to retrieve information for.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the user information.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/users?username=" + user
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def edit_serial_port_config(self, config):
        """
        Edits the serial port configuration on the WTI device.

        Args:
            config (dict, optional): A dictionary containing the serial port configuration to be applied.
                   
                {
				  "serialports": {
				    "port": 4,
				    "portname": "RouterLabel",
				    "baud": 7,
				    "handshake": 1,
				    "stopbits": 1,
				    "parity": 0,
				    "mode": 0,
				    "cmd": 0,
				    "seq": 1,
				    "tout": 1,
				    "echo": 0,
				    "break": 0,
				    "logoff": "^H"
				  }
				}

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the response of the configuration edit.
                If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/serialports"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def add_new_user(self, config):
        """
        Add a new user using the provided configuration.

        Args:
            config (dict): A dictionary containing the configuration details for the new user.
                        The dictionary should follow the format:
                        {
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

        Returns:
            dict or None: A dictionary containing the response data if the user was successfully added,
                        or None if there was an error or the request was unsuccessful.

        Raises:
            Any exceptions raised by the requests library.

        Note:
            - This method assumes that the base_url, username, and password variables are already defined.
            - This method uses the requests library to send a POST request to the API endpoint.
            - The response JSON format and possible error codes should be documented in the API documentation.
        """
        url = f"{self.base_url}/api/v2/config/users"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def edit_user(self, config):
        """
        Edit an existing user using the provided configuration.

        Args:
            config (dict): A dictionary containing the configuration details for the user to be edited.
                        The dictionary should follow the format:
                        {
                            "users": {
                                "username": "user",
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

        Returns:
            dict or None: A dictionary containing the response data if the user was successfully edited,
                        or None if there was an error or the request was unsuccessful.

        Raises:
            Any exceptions raised by the requests library.

        Note:
            - This method assumes that the base_url, username, and password variables are already defined.
            - This method uses the requests library to send a PUT request to the API endpoint.
            - The response JSON format and possible error codes should be documented in the API documentation.
            - The `username` field in the config dictionary specifies the user to be edited.
        """
        url = f"{self.base_url}/api/v2/config/users"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def delete_user(self, username):
        """
            Delete an existing user specified by the username.

            Args:
                username (str): The username of the user to be deleted.

            Returns:
                dict or None: A dictionary containing the response data if the user was successfully deleted,
                            or None if there was an error or the request was unsuccessful.

            Raises:
                Any exceptions raised by the requests library.

            Note:
                - This method assumes that the base_url, username, and password variables are already defined.
                - This method uses the requests library to send a DELETE request to the API endpoint.
                - The response JSON format and possible error codes should be documented in the API documentation.
            """
        url = f"{self.base_url}/api/v2/config/users?username=" + username
        response = requests.delete(url, auth=(self.username, self.password), verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_all_serial_port_config(self):
        """
        Retrieves the configuration of all serial ports from the WTI device.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the serial port configurations.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/serialports"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
    
    def get_specific_serial_port_config(self, serial_port):
        """
        Retrieves the configuration of a specific serial port from the WTI device.

        Args:
            serial_port (str): The name or identifier of the serial port to retrieve configuration for.

        Returns:
            dict or int: If the API request is successful, returns a dictionary containing the serial port configuration.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/serialports?serialports=" + str(serial_port)
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_aaa_server_config(self, aaa_server='radius'):
        """Retrieve the configuration of an WTI AAA server.

        Args:
            aaa_server (str, optional): The type of AAA server to retrieve the configuration for. 
                                    Valid options are 'radius' (default) or 'tacacs'. 

        Returns:
            dict or None: If the configuration is successfully retrieved (status code 200), 
                        the JSON response containing the configuration details is returned as a dictionary.
                        If there is an error or the configuration cannot be retrieved, None is returned.
        """
        url = f"{self.base_url}/api/v2/config/aaaserver?service=" + aaa_server
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_network_interface_config(self, interface):
        """
        Retrieves the configuration of a network interface.

        Args:
            interface (str): The name of the interface to retrieve configuration for. Defaults to None to collect
            all the interface's configuration.

        Returns:
            dict or int or str: If `interface` is None, returns a dictionary containing the configuration
            of all network interfaces. If `interface` is specified and found, returns a dictionary
            representing the configuration of the specified interface. If `interface` is specified but not found,
            returns a string with an error message indicating that no interface was found with the specified name.
            If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/interface"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if interface is None:
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code
            
        elif interface:
            for int in response.json()['interface']:
                if int['name'] == interface:
                    return int
                
        return f"No interface found with the name '{interface}'"
        
    def edit_network_interface_config(self, config):
        """
        Edits the configuration of a network interface.

        Args:
            config (dict): The configuration data for the network interface.

        Returns:
            dict or int: If the configuration is successfully updated, returns a dictionary containing
            the updated configuration. If an error occurs during the API request, returns an integer
            representing the HTTP status code.

        Example:
            The `config` parameter should be a dictionary with the following structure:

            {
            "interface": {
                "name": "eth0",
                "ietf-ipv4": {
                "address": [
                    {
                    "ip": "10.60.11.101",
                    "netmask": "255.255.255.240",
                    "gateway": "10.60.11.97"
                    }
                ]
                }
            }
            }
        """
        url = f"{self.base_url}/api/v2/config/interface"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_config_hostname(self):
        """
        Retrieves the hostname of the device.

        Returns:
            dict or int: If the hostname is successfully retrieved, a dictionary is returned containing
            the hostname information. If an error occurs during the API request, an integer is returned
            representing the HTTP status code.

        Raises:
            ConnectionError: If there is an issue establishing a connection to the device.

        Examples:
            The returned dictionary may have the following structure:

            {
            "status": {"code": "0","text": "ok"},
            "unitid": {
                "timestamp": "2023-05-25T18:23:08+00:00",
                "hostname": "DEV2466S01",
                "location": "",
                "assettag": ""
            }
            }
        """
        url = f"{self.base_url}/api/v2/config/hostname"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def edit_config_hostname(self, config):
        """
        Edits the hostname configuration of the device.

        Args:
            config (dict): A dictionary representing the new hostname configuration. It should have the following structure:
            {
            "unitid": {
                "hostname": "DSMLABIRVINE",
                "location": "RACK12IRVINE",
                "assettag": "1028561"
            }
            }

        Returns:
            dict or int: If the hostname is successfully edited, returns a dictionary containing the updated hostname configuration.
                If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/hostname"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_config_timedate(self):
        """
        Retrieves the current time and date configuration of the device.

        Returns:
            dict or int: If the request is successful, returns a dictionary containing the time and date configuration
            of the device. If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/timedate"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def edit_config_timedate(self, config):
        """
        Edits the time and date configuration of the device.

        Args:
            config (dict): A dictionary representing the new time and date configuration. It should have the following structure:
            
            config={
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

        Returns:
            dict or int: If the time and date configuration is successfully edited, returns a dictionary containing the updated configuration.
                If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/timedate"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_config_web_service(self):
        """
        Retrieves the configuration of the device's web service.

        Returns:
            dict or int: If the web service configuration is successfully retrieved, returns a dictionary containing the configuration.
                If an error occurs during the API request, returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/web"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_config_snmp_trap(self):
        """
        Retrieves the SNMP trap configuration.

        Returns:
            dict or int: If the API request is successful and returns a status code of 200,
            returns a dictionary containing the SNMP trap configuration.
            If an error occurs during the API request, returns an integer representing
            the HTTP status code.
        """
        url = f"{self.base_url}/api/v2/config/snmptrap"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def edit_config_snmp_trap(self, config):
        """    
        Modifies the SNMP trap configuration.

        Args:
            config (dict): A dictionary containing the updated SNMP trap configuration.

            config = 
                {
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
        Returns:
            dict or int: If the API request is successful and returns a status code of 200,
            returns a dictionary containing the updated SNMP trap configuration.
            If an error occurs during the API request, returns an integer representing
            the HTTP status code.
        """

        url = f"{self.base_url}/api/v2/config/snmptrap"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_config_snmp_access(self):
        """
        Retrieves the SNMP access configuration from the device.

        Returns:
            dict or int: If the SNMP access configuration is successfully retrieved, returns a dictionary
            containing the SNMP access configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/snmpaccess"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def edit_config_snmp_access(self, config):
        """
        Edits the SNMP access configuration on the device.

        Args:
            config (dict): A dictionary containing the new SNMP access configuration to be applied.

            config = 
                {
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
        Returns:
            dict or int: If the SNMP access configuration is successfully edited, returns a dictionary
            containing the updated SNMP access configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/snmpaccess"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_config_ip_tables(self):
        """
        Retrieves the IP tables configuration from the device.

        Returns:
            dict or int: If the IP tables configuration is successfully retrieved, returns a dictionary
            containing the IP tables configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/iptables"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def edit_config_ip_tables(self, config):
        """
        Edits the IP tables configuration on the device.

        Args:
            config (dict): A dictionary containing the new IP tables configuration to be applied.

            config = 
                {
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
            
        Returns:
            dict or int: If the IP tables configuration is successfully edited, returns a dictionary
            containing the updated IP tables configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/iptables"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_config_syslog_server(self):
        """
        Retrieves the configuration of the syslog server from the device.

        Returns:
            dict or int: If the syslog server configuration is successfully retrieved, returns a dictionary
            containing the syslog server configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/syslogserver"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def edit_config_syslog_server(self, config):
        """
        Edits the configuration of the syslog server on the device.

        Args:
            config (dict): A dictionary containing the new syslog server configuration to be applied.
            
            config = 
                {
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
        Returns:
            dict or int: If the syslog server configuration is successfully edited, returns a dictionary
            containing the updated syslog server configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/syslogserver"
        headers = {'Content-Type': 'application/json'}
        response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def get_config_syslog_client(self):
        """
        Retrieves the configuration of the syslog client from the device.

        Returns:
            dict or int: If the syslog client configuration is successfully retrieved, returns a dictionary
            containing the syslog client configuration details. If an error occurs during the API request,
            returns an integer representing the HTTP status code.

        """
        url = f"{self.base_url}/api/v2/config/syslogclient"
        response = requests.get(url, auth=(self.username, self.password), verify=False)
        response.close()
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def edit_config_syslog_client(self, config):
            """
            Edits the configuration of the syslog client on the device.

            Args:
                config (dict): A dictionary containing the new syslog client configuration to be applied.

                config = 
                    {
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
                
            Returns:
                dict or int: If the syslog client configuration is successfully edited, returns a dictionary
                containing the updated syslog client configuration details. If an error occurs during the API request,
                returns an integer representing the HTTP status code.

            """
            url = f"{self.base_url}/api/v2/config/syslogclient"
            headers = {'Content-Type': 'application/json'}
            response = requests.put(url, auth=(self.username, self.password), headers=headers, json=config, verify=False)
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code
            
