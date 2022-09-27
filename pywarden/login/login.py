#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pywarden.login import status
from pywarden.login import unlock
from pywarden.logger import logger
import pexpect

from pywarden.pywarden import handle_config

def bw_login():
    BW_STATUS = status.get_status()
    if BW_STATUS == "unlocked":
        if handle_config.VERBOSE == True:
            logger.pywarden_logger(Payload="Bitwarden is already unlocked", Color="green", ErrorExit=False, Exit=False)
    if BW_STATUS == "locked":
        if handle_config.VERBOSITY == True:
            logger.pywarden_logger(Payload="Bitwarden is locked, attempting to unlock", Color="yellow", ErrorExit=False, Exit=False)
        unlock.bw_unlock()

    if BW_STATUS == "unauthenticated":
        if handle_config.VERBOSITY == True:
            logger.pywarden_logger(Payload="Bitwarden is unauthenticated, attempting to login", Color="yellow", ErrorExit=False, Exit=False)
        child = pexpect.spawn('bw', ['login', '--apikey'], encoding='utf-8')
        child.expect('client_id')
        child.sendline(handle_config.BITWARDEN_API_CLIENT_ID)
        child.expect('client_secret')
        child.sendline(handle_config.BITWARDEN_API_CLIENT_SECRET)
        child.expect(pexpect.EOF)
        BW_STATUS = status.get_status()
        if BW_STATUS == "locked":
            logger.pywarden_logger(Payload="Bitwarden is locked, attempting to unlock", Color="blue", ErrorExit=False, Exit=False)
            unlock.bw_unlock()
