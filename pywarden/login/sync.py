#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect

from pywarden.pywarden import handle_config
from pywarden.logger import logger
from pywarden.classes import classes

def bw_sync():
    child = pexpect.spawn('bw', ['sync'], encoding='utf-8')
    child.expect(pexpect.EOF)
    global BITWARDEN_SYNC_RESULT
    BITWARDEN_SYNC_RESULT = child.before.splitlines()[-1]
    if 'complete' != None and 'complete' in BITWARDEN_SYNC_RESULT:
        if handle_config.VERBOSITY == True:
            logger.pywarden_logger(Payload="Bitwarden sync complete", Color="green", ErrorExit=False, Exit=False)
    elif 'failed' != None and 'failed' in BITWARDEN_SYNC_RESULT:
        if handle_config.VERBOSITY == True:
            logger.pywarden_logger(Payload="Bitwarden sync failed", Color="red", ErrorExit=True, Exit=False)
