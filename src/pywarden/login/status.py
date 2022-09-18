#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json 
import subprocess

from pywarden import handle_config

from classes import classes

def get_status(SESSION_KEY=None, FETCH_userEmail=False):
    if SESSION_KEY == None:
        BITWARDEN_STATUS = subprocess.check_output('bw status', shell=True, encoding='utf-8')
        BITWARDEN_STATUS_JSON = json.loads(BITWARDEN_STATUS)
        BITWARDEN_STATUS_VALUE = BITWARDEN_STATUS_JSON['status']
        return BITWARDEN_STATUS_VALUE
    if SESSION_KEY != None:
        # Format string
        BITWARDEN_STATUS_FORMAT = 'bw status --session={}'.format(SESSION_KEY)
        BITWARDEN_STATUS = subprocess.check_output(BITWARDEN_STATUS_FORMAT, shell=True, encoding='utf-8')
        BITWARDEN_STATUS_JSON = json.loads(BITWARDEN_STATUS)
        BITWARDEN_STATUS_VALUE = BITWARDEN_STATUS_JSON['status']
        print(f"{classes.bcolors.OKGREEN}Status: {BITWARDEN_STATUS_VALUE}{classes.bcolors.ENDC}")
        return BITWARDEN_STATUS_VALUE
    if FETCH_userEmail == True:
        BITWARDEN_STATUS = subprocess.check_output('bw status', shell=True, encoding='utf-8')
        BITWARDEN_STATUS_JSON = json.loads(BITWARDEN_STATUS)
        BITWARDEN_STATUS_VALUE = BITWARDEN_STATUS_JSON['userEmail']
        return BITWARDEN_STATUS_VALUE
