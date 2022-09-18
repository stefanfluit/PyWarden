#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import base64
import json

from login import sync
from cli import get_items
from pywarden import handle_config
from classes import classes
from login import unlock

def bw_create_item(ITEM_NAME, ITEM_USERNAME, ITEM_PASSWORD, ITEM_URL, ITEM_NOTES, ITEM_FOLDER, ITEM_COLLECTION, ITEM_ORG_COLLECTION):
    # Store templates in variables
    get_template = subprocess.check_output(f'bw get template item --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
    get_login_template = subprocess.check_output(f'bw get template item.login.uri --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
    get_login_item_template = subprocess.check_output(f'bw get template item.login --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')

    # Convert templates to JSON
    get_template_json = json.loads(get_template)
    get_login_template_json = json.loads(get_login_template)
    get_login_item_template_json = json.loads(get_login_item_template)

    # Append arrays
    collectionIds=[]
    collectionIds.append(get_items.get_collection_id(ITEM_ORG_COLLECTION))

    # Set variables
    get_template_json['organizationId'] = get_items.get_organization_id()
    get_template_json['name'] = ITEM_NAME
    get_template_json['collectionIds'] = collectionIds

    # Set login variables
    if ITEM_URL != None:
        if ITEM_URL != '':
            get_login_template_json['match'] = True
            get_login_template_json['uri'] = ITEM_URL
        else:
            get_login_template_json['match'] = None
            get_login_template_json['uri'] = None

    # Set login item variables
    get_login_item_template_json['username'] = ITEM_USERNAME
    get_login_item_template_json['password'] = ITEM_PASSWORD
    get_login_item_template_json['uris'] = [get_login_template_json]
    get_login_item_template_json['totp'] = None

    # Set notes
    if ITEM_NOTES != None:
        if ITEM_NOTES != '':
            get_template_json['notes'] = ITEM_NOTES
        else:
            get_template_json['notes'] = None

    # Combine
    get_template_json['login'] = get_login_item_template_json

    # Encode the json into base64
    b64 = str(base64.b64encode(json.dumps(get_template_json).encode('utf-8')))
    b64 = b64.replace("b'", "").replace("'", "")
    subprocess.check_output(f'bw create item {b64} --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
    sync.bw_sync()
    if get_items.check_if_object_exists('item', ITEM_NAME) == True:
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.OKGREEN}Item created!{classes.bcolors.ENDC}")
            exit(0)
    else:
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.WARNING}Item creation failed!{classes.bcolors.ENDC}")
        exit(1)