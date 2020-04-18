#!/bin/python
from __future__ import print_function
import sys
import logging
from argparse import ArgumentParser
import csv
import requests
import json
from requests.auth import HTTPBasicAuth
from dnac_config import *
import urllib3

template_url="https://10.3.24.230/dna/intent/api/v1/template-programmer/template"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token():
    url="https://10.3.24.230/dna/system/api/v1/auth/token"
    response=requests.post(url,auth=(USERNAME, PASSWORD),verify=False)
    token=response.json()['Token']
    return token

def list_templates():
    url=template_url
    headers={"X-Auth-Token": "{}".format(Token),"Content-type": "application/json"}
    response=requests.get(url=url, headers=headers, verify=False)
    templates=response.json()
    return templates

def get_template(tid):
    url=(template_url+"/"+tid)
    response=requests.get(url=url, headers=headers, verify=False)
    template_data=response.json()
    return template_data

Token=get_token()
headers={"X-Auth-Token": "{}".format(Token),"Content-type": "application/json"}

_,*args=sys.argv
arguments=args
if arguments == []:
    for template in list_templates():
        print("{name}".format(name=template["name"],project=template["projectName"]))
else:
    for template in list_templates():
        name_key=[(template['name'])]
        if name_key == arguments:
            templateid=(template['templateId'])
            print('template name: {name}\ntemplateid: {tid}'.format(name=template["name"],tid=template['templateId']))
            print('\n*Required Parameters for this template\n')
            for data in get_template(templateid)['templateParams']:
                isRequired=(data['required'])
                if isRequired == True:
                    print('*{0}'.format(data['parameterName']))
                else:
                    print('{0}'.format(data['parameterName']))

