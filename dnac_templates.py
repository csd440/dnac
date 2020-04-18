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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token():
    url="https://10.3.24.230/dna/system/api/v1/auth/token"
    response=requests.post(url,auth=(USERNAME, PASSWORD),verify=False)
    token=response.json()['Token']
    return token

def list_templates(_args):
    print(args)



Token=get_token()
list_templates(*args)

