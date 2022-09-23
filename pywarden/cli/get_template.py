#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.classes import classes
from pywarden.pywarden import handle_config
from pywarden.login import unlock
from pywarden.logger import logger

import subprocess
import json

def get_template(template_type=None):
    if template_type == None:
        if handle_config.VERBOSITY == True:
            logger.pywarden_logger(Payload="No template type specified", Color="red", ErrorExit=True, Exit=1)
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
