#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.pywarden import handle_config
from pywarden.classes import classes
from pywarden.cli import get_items
from pywarden.api import get_ids
from pywarden.login import unlock
from pywarden.logger import logger
from pywarden.login import sync
import subprocess
import json
import base64

def ensure_org_collection(org_collection_name=None, access_group=None, debug_mode=False):
    if org_collection_name == None:
        if org_collection_name != '':
            logger.pywarden_logger(Payload="org_collection_name is not defined", Color="red", ErrorExit=True, Exit=False)
    if access_group == None:
        if access_group != '':
            logger.pywarden_logger(Payload="access_group is not defined", Color="red", ErrorExit=True, Exit=False)
    else:
        if get_items.check_if_object_exists('collection', org_collection_name) == True:
            if handle_config.VERBOSITY == True:
                logger.pywarden_logger(Payload="Organization collection already exists", Color="green", ErrorExit=False, Exit=False)
        else:
            access_group_id = get_ids.get_group_id(access_group)
            get_template = subprocess.check_output(f'bw get template org-collection --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
            get_template_json = json.loads(get_template)
            get_template_json['name'] = org_collection_name
            get_template_json['organizationId'] = get_items.get_organization_id()
            get_template_json['groups'].pop(1)
            # Change the group ID to the access_group group ID
            get_template_json['groups'][0]['id'] = access_group_id

            # If debug mode is true, print the json
            if debug_mode == True:
                print(json.dumps(get_template_json, indent=4))

            # Encode the json into base64
            b64 = str(base64.b64encode(json.dumps(get_template_json).encode('utf-8')))
            # Strip the b' and ' from the string
            b64 = b64.replace("b'", "").replace("'", "")

            subprocess.check_output(f'bw create org-collection {b64} --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
            sync.bw_sync()
            if get_items.check_if_object_exists('collection', org_collection_name) == True:
                if handle_config.VERBOSITY == True:
                    logger.pywarden_logger(Payload="Organization collection created", Color="green", ErrorExit=False, Exit=False)
                else:
                    pass
            else:
                if handle_config.VERBOSITY == True:
                    logger.pywarden_logger(Payload="Organization collection could not be created", Color="red", ErrorExit=True, Exit=False)
                else:
                    exit(1)
