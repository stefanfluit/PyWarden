#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from login import status
from login import unlock
import pexpect

from pywarden import handle_config

from classes import classes

def bw_login():
    BW_STATUS = status.get_status()
    if BW_STATUS == "unlocked":
        if handle_config.VERBOSE == True:
            print(f"{classes.bcolors.OKGREEN}Bitwarden is unlocked!{classes.bcolors.ENDC}")
    if BW_STATUS == "locked":
        if handle_config.VERBOSITY == True:
            print(f"{classes.bcolors.OKGREEN}Bitwarden is locked!{classes.bcolors.ENDC}")
        unlock.bw_unlock()

    if BW_STATUS == "unauthenticated":
        print(f"{classes.bcolors.WARNING}Bitwarden is unauthenticated!{classes.bcolors.ENDC}")
        child = pexpect.spawn('bw', ['login', '--apikey'], encoding='utf-8')
        child.expect('client_id')
        child.sendline(handle_config.BITWARDEN_API_CLIENT_ID)
        child.expect('client_secret')
        child.sendline(handle_config.BITWARDEN_API_CLIENT_SECRET)
        child.expect(pexpect.EOF)
        BW_STATUS = status.get_status()
        if BW_STATUS == "locked":
            print(f"{classes.bcolors.WARNING}Succesfully logged in, unlocking Vault now.{classes.bcolors.ENDC}")
            unlock.bw_unlock()
