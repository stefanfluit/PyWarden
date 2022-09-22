#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from pywarden.classes import classes
import json

from pywarden.pywarden import handle_config
from pywarden.login import unlock

def get_organization_id():
    get_organization_name = subprocess.check_output(f'bw list organizations --pretty --nointeraction --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
    get_organization_name_json = json.loads(get_organization_name)
    return(get_organization_name_json[0]['id'])

def get_collection_id(COLLECTION_NAME):
    get_collection_id = subprocess.check_output(f'bw list collections --pretty --nointeraction --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
    get_collection_id_json = json.loads(get_collection_id)
    for collection in get_collection_id_json:
        if collection['name'] == COLLECTION_NAME:
            if handle_config.VERBOSITY == True:
                print(f"{classes.bcolors.OKGREEN}Found collection ID: {collection['id']}{classes.bcolors.ENDC}")
            return(collection['id'])

def check_if_object_exists(object_type, object_name):
    if object_type == 'organization':
        if object_name in subprocess.check_output(f'bw list organizations --pretty --nointeraction --session={unlock.bw_unlock()}', shell=True, encoding='utf-8'):
            print(f"{classes.bcolors.OKGREEN}Found organization: {object_name}{classes.bcolors.ENDC}")
            return True
        else:
            print(f"{classes.bcolors.FAIL}Organization not found: {object_name}{classes.bcolors.ENDC}")
            return False
    if object_type == 'collection':
        if object_name in subprocess.check_output(f'bw list collections --pretty --nointeraction --organizationid={get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8'):
            print(f"{classes.bcolors.OKGREEN}Found collection: {object_name}{classes.bcolors.ENDC}")
            return True
        else:
            print(f"{classes.bcolors.FAIL}Collection not found: {object_name}{classes.bcolors.ENDC}")
            return False
    if object_type == 'item':
        if object_name in subprocess.check_output(f'bw list items --pretty --nointeraction --organizationid={get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8'):
            print(f"{classes.bcolors.OKGREEN}Found item: {object_name}{classes.bcolors.ENDC}")
            return True
        else:
            print(f"{classes.bcolors.FAIL}Item not found: {object_name}{classes.bcolors.ENDC}")
            return False
