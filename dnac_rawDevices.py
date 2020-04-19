from dnac_config import *
from collections import Counter
import json

url="https://10.3.24.230/dna/intent/api/v1/network-device"
headers={"X-Auth-Token": "{}".format(Token),"Content-type": "application/json"}

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


devices=list_devices()
output=json.dumps(devices,indent=4)
print(output)
