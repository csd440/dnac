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
