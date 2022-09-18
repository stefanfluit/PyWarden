#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from classes import classes
from pywarden import handle_config
from login import unlock
import subprocess
import json

def get_template(template_type=None):
    if template_type == None:
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.WARNING}No template type specified, skipping template retrieval.{classes.bcolors.ENDC}")
            exit(1)
        else:
            exit(1)
    else:
        if template_type == 'org-collection':
            get_template = subprocess.check_output(f'bw get template org-collection --pretty --nointeraction --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
            get_template_json = json.loads(get_template)
            print(json.dumps(get_template_json, indent=4, sort_keys=True))
        if template_type == 'item':
            get_template = subprocess.check_output(f'bw get template item --pretty --nointeraction --session={unlock.bw_unlock()}', shell=True, encoding='utf-8')
            get_template_json = json.loads(get_template)
            print(json.dumps(get_template_json, indent=4, sort_keys=True))
