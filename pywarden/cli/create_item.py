#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import base64
import json

from pywarden.login import sync
from pywarden.cli import get_items
from pywarden.pywarden import handle_config
from pywarden.logger import logger
from pywarden.login import unlock
from pywarden.cli import create_collection

def bw_create_org_item(ITEM_NAME, ITEM_USERNAME, ITEM_PASSWORD, ITEM_URL, ITEM_NOTES, ITEM_FOLDER, ITEM_COLLECTION, ITEM_ORG_COLLECTION):
    # Ensure all variables are defined, error out if not.
    if ITEM_NAME is None:
        if ITEM_NAME != "":
            logger.pywarden_logger(Payload="ITEM_NAME is not defined", Color="red", ErrorExit=True, Exit=1)
    if ITEM_USERNAME is None:
        if ITEM_USERNAME != "":
            logger.pywarden_logger(Payload="ITEM_USERNAME is not defined", Color="red", ErrorExit=True, Exit=1)
    if ITEM_PASSWORD is None:
        if ITEM_PASSWORD != "":
            logger.pywarden_logger(Payload="ITEM_PASSWORD is not defined", Color="red", ErrorExit=True, Exit=1)
    if ITEM_ORG_COLLECTION is None:
        if ITEM_ORG_COLLECTION != "":
            logger.pywarden_logger(Payload="ITEM_ORG_COLLECTION is not defined", Color="red", ErrorExit=True, Exit=1)

    # Ensure the org-collection exists
    create_collection.ensure_org_collection(ITEM_ORG_COLLECTION)

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
            logger.pywarden_logger(Payload=f"Successfully created item {ITEM_NAME}", Color="green")
            exit(0)
    else:
        if handle_config.VERBOSITY == True:
            logger.pywarden_logger(Payload=f"Failed to create item {ITEM_NAME}", Color="red")
        exit(1)
