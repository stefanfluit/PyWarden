#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect

from pywarden.pywarden import handle_config

from pywarden.classes import classes

def bw_sync():
    child = pexpect.spawn('bw', ['sync'], encoding='utf-8')
    child.expect(pexpect.EOF)
    global BITWARDEN_SYNC_RESULT
    BITWARDEN_SYNC_RESULT = child.before.splitlines()[-1]
    if 'complete' != None and 'complete' in BITWARDEN_SYNC_RESULT:
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.OKGREEN}Sync complete!{classes.bcolors.ENDC}")
    elif 'failed' != None and 'failed' in BITWARDEN_SYNC_RESULT:
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.WARNING}Bitwarden sync failed!{classes.bcolors.ENDC}")
            exit(6)
