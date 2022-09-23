#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from pywarden.classes import classes
import json

from pywarden.cli import get_items
from pywarden.logger import logger

from pywarden.pywarden import handle_config
from pywarden.login import unlock

def list_all(list_type=None):
    if handle_config.VERBOSITY == True:
        logger.pywarden_logger(Payload=f"Listing all {list_type}", Color="green", ErrorExit=False, Exit=None)

    if list_type == 'organizations':
        get_all_organizations = subprocess.check_output(f'bw list organizations --pretty --nointeraction --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
        get_all_organizations_json = json.loads(get_all_organizations)
        print(json.dumps(get_all_organizations_json, indent=4, sort_keys=True))

    if list_type == 'collections':
        get_all_collections = subprocess.check_output(f'bw list collections --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
        get_all_collections_json = json.loads(get_all_collections)
        print(json.dumps(get_all_collections_json, indent=4, sort_keys=True))

    if list_type == 'items':
        get_all_entries = subprocess.check_output(f'bw list items --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
        get_all_entries_json = json.loads(get_all_entries)
        print(json.dumps(get_all_entries_json, indent=4, sort_keys=True))

    if list_type == 'folders':
        get_all_folders = subprocess.check_output(f'bw list folders --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
        get_all_folders_json = json.loads(get_all_folders)
        print(json.dumps(get_all_folders_json, indent=4, sort_keys=True))

    if list_type == 'org-members':
        get_all_org_members = subprocess.check_output(f'bw list org-members --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
        get_all_org_members_json = json.loads(get_all_org_members)
        print(json.dumps(get_all_org_members_json, indent=4, sort_keys=True))

    if list_type == 'org-collections':
        get_all_org_collections = subprocess.check_output(f'bw list org-collections --pretty --nointeraction --organizationid={get_items.get_organization_id()} --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
        get_all_org_collections_json = json.loads(get_all_org_collections)
        print(json.dumps(get_all_org_collections_json, indent=4, sort_keys=True))
