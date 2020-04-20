'''
Script Name: dnac_devices.py
Author: Chris Day
Description: Get a list of devices to provide the information that is important to the customer.
List the number of device types and quantity of each device type on the network
Change History:
Version, Author, Date, Comments
0.1, chris day, 20.04.2020, initial script
'''
from dnac_config import *
from collections import Counter
import sys

url="https://10.3.24.230/dna/intent/api/v1/network-device"
headers={"X-Auth-Token": "{}".format(Token),"Content-type": "application/json"}
count=0

def list_devices():
    response=requests.get(url=url, headers=headers, verify=False)
    devices=response.json()
    return devices
def sort_devices():
    response=requests.get(url=url, headers=headers, verify=False)
    devices=response.json()
    platforms=[]
    for device in devices['response']:
        platforms.append(device['platformId'])
    totalPlatforms=Counter(platforms)
    totalPlatforms=dict(totalPlatforms)
    for key,value in totalPlatforms.items():
        print('Total',key,':',value)
_,*args=sys.argv
arguments=args
for device in list_devices()['response']:
    print('Hostname:{name}\nDevice-Id:{ID}\nSerial#:{sn}\nIP Address:{ip}\nType:{Type}\nSoftware:{software}\nReachability:{reachable}\n'.format(name=device['hostname'],sn=device['serialNumber'],ip=device['managementIpAddress'],Type=device['platformId'],software=device['softwareVersion'],reachable=device['reachabilityStatus'],ID=device['id']))
    count +=1

sort_devices()
print('Total Devices:',count)
