#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.pywarden import handle_config
from pywarden.classes import classes
from pywarden.cli import get_items
from pywarden.api import get_ids
from pywarden.login import unlock
import subprocess
import json
import base64

def ensure_org_collection(org_collection_name=None):
    if org_collection_name == None:
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.WARNING}No org collection name specified, skipping org collection creation.{classes.bcolors.ENDC}")
            exit(1)
        else:
            exit(1)
    else:
        if get_items.check_if_object_exists('collection', org_collection_name) == True:
            if handle_config.VERBOSITY == True:
                print(f"{classes.bcolors.WARNING}Organization: {org_collection_name} already exists!{classes.bcolors.ENDC}")
            exit(0)
        else:
            production_id = get_ids.get_group_id("Production")
            get_template = subprocess.check_output(f'bw get template org-collection --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
            get_template_json = json.loads(get_template)
            get_template_json['name'] = org_collection_name
            get_template_json['organizationId'] = get_items.get_organization_id()
            get_template_json['groups'].pop(1)
            # Change the group ID to the production group ID
            get_template_json['groups'][0]['id'] = production_id
            print(json.dumps(get_template_json, indent=4))
            # Encode the json into base64
            b64 = str(base64.b64encode(json.dumps(get_template_json).encode('utf-8')))
            # Strip the b' and ' from the string
            b64 = b64.replace("b'", "").replace("'", "")
            subprocess.check_output(f'bw create org-collection {b64} --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
            unlock.bw_sync()
            if get_items.check_if_object_exists('collection', org_collection_name) == True:
                if handle_config.VERBOSITY == True:
                    print(f"{classes.bcolors.OKGREEN}Organization collection: {org_collection_name} created!{classes.bcolors.ENDC}")
                else:
                    pass
            else:
                if handle_config.VERBOSITY == True:
                    print(f"{classes.bcolors.WARNING}Organization collection: {org_collection_name} creation failed!{classes.bcolors.ENDC}")
                    exit(1)
                else:
                    exit(1)
