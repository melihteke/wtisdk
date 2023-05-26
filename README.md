# WTI-SDK
The WTISDK is a Python class that provides an interface for interacting with a WTI device. It allows you to retrieve various information and perform configuration changes on the device using its API. This README provides an overview of the class and its methods, along with examples of how to use them.

## Prerequisites
Before using the WtiClient class, ensure that you have the following prerequisites:

Python 3.x installed on your system.
The requests library installed. You can install it using pip install requests.

## Usage
To use the WtiClient class, follow these steps:

### Installation
```sh
pip install wtisdk
```


### Basic Usage
```sh
(.venv) [mteke1@n6lans00001 test_infra]$ ipython
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
 'serialnumber': '01910453453191131',
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
