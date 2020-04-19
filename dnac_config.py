import requests
import json
import urllib3

USERNAME=('adm-cday')
PASSWORD=('N0tnight!')
DNAC_IP=("10.3.24.230")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token():
    url="https://10.3.24.230/dna/system/api/v1/auth/token"
    response=requests.post(url,auth=(USERNAME, PASSWORD),verify=False)
    token=response.json()['Token']
    return token

Token=get_token()
