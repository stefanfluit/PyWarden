#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path
import validators

from pywarden.logger import logger
from pywarden.pywarden import conf_file

def manage_configuration(supress=False, show_path=False):

    config_file = conf_file.get_conf_file()

    if show_path:
        # Format a string with a message and the path to the config file
        message = "The path to the found config file is: " + str(config_file)
        print(message)

    if os.path.isfile(config_file):
        with open(config_file, "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    bw_passwd_length = config['BITWARDEN_PASSWORD_LENGTH']
    if isinstance(bw_passwd_length, int):
        if config['BITWARDEN_PASSWORD_LENGTH'] < 8:
            print('BITWARDEN_PASSWORD_LENGTH is not long enough, minumum length is 8')
            exit(2)
        else:
            global BITWARDEN_PASSWORD_LENGTH
            BITWARDEN_PASSWORD_LENGTH = int(config['BITWARDEN_PASSWORD_LENGTH'])
    else:
        logger.pywarden_logger(Payload="BITWARDEN_PASSWORD_LENGTH is not an integer", Color="red", ErrorExit=True, Exit=False)

    bw_url = config['BITWARDEN_SERVER_URL']
    if config['BITWARDEN_SERVER_URL'] != None:
        if validators.url(bw_url):
            global BITWARDEN_URL
            BITWARDEN_URL = config['BITWARDEN_SERVER_URL']
        else:
            logger.pywarden_logger(Payload="BITWARDEN_SERVER_URL is not a valid URL", Color="red", ErrorExit=True, Exit=False)
    else:
        logger.pywarden_logger(Payload="BITWARDEN_SERVER_URL is not set", Color="red", ErrorExit=True, Exit=False)

    bw_public_api_url = config['BITWARDEN_PUBLIC_API_URL']
    if config['BITWARDEN_PUBLIC_API_URL'] != None:
        if validators.url(bw_public_api_url):
            global BITWARDEN_PUBLIC_API_URL
            BITWARDEN_PUBLIC_API_URL = config['BITWARDEN_PUBLIC_API_URL']
        else:
            logger.pywarden_logger(Payload="BITWARDEN_PUBLIC_API_URL is not a valid URL", Color="red", ErrorExit=True, Exit=False)
    else:
        logger.pywarden_logger(Payload="BITWARDEN_PUBLIC_API_URL is not set", Color="red", ErrorExit=True, Exit=False)

    bw_auth_endpoint = config['BITWARDEN_AUTH_ENDPOINT']
    if config['BITWARDEN_AUTH_ENDPOINT'] != None:
        if validators.url(bw_auth_endpoint):
            global BITWARDEN_AUTH_ENDPOINT
            BITWARDEN_AUTH_ENDPOINT = config['BITWARDEN_AUTH_ENDPOINT']
        else:
            logger.pywarden_logger(Payload="BITWARDEN_AUTH_ENDPOINT is not a valid URL", Color="red", ErrorExit=True, Exit=False)
    else:
        logger.pywarden_logger(Payload="BITWARDEN_AUTH_ENDPOINT is not set", Color="red", ErrorExit=True, Exit=False)
    
    bw_client_id = config['BITWARDEN_API_CLIENT_ID']
    if config['BITWARDEN_API_CLIENT_ID'] != None:
        if config['BITWARDEN_API_CLIENT_ID'] == '':
            logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_ID is not set", Color="red", ErrorExit=True, Exit=False)
        else:
            if isinstance(bw_client_id, str):
                if len(bw_client_id) < 40:
                    logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_ID is not long enough, minimum length is 40", Color="red", ErrorExit=True, Exit=False)
                else:
                    global BITWARDEN_API_CLIENT_ID
                    BITWARDEN_API_CLIENT_ID = config['BITWARDEN_API_CLIENT_ID']
            else:
                logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_ID is not a string", Color="red", ErrorExit=True, Exit=False)
    else:
        logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_ID is not set", Color="red", ErrorExit=True, Exit=False)
    
    bw_client_secret = config['BITWARDEN_API_CLIENT_SECRET']
    if config['BITWARDEN_API_CLIENT_SECRET'] != None:
        if config['BITWARDEN_API_CLIENT_SECRET'] == '':
            logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_SECRET is not set", Color="red", ErrorExit=True, Exit=False)
        else:
            if isinstance(bw_client_secret, str):
                if len(bw_client_secret) < 30:
                    logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_SECRET is not long enough, minimum length is 30", Color="red", ErrorExit=True, Exit=False)
                else:
                    global BITWARDEN_API_CLIENT_SECRET
                    BITWARDEN_API_CLIENT_SECRET = config['BITWARDEN_API_CLIENT_SECRET']
            else:
                logger.pywarden_logger(Payload="BITWARDEN_API_CLIENT_SECRET is not a string", Color="red", ErrorExit=True, Exit=False)
    
    bw_master_password = config['BITWARDEN_MASTER_PASSWORD']
    if config['BITWARDEN_MASTER_PASSWORD'] != None:
        if config['BITWARDEN_MASTER_PASSWORD'] == '':
            logger.pywarden_logger(Payload="BITWARDEN_MASTER_PASSWORD is not set", Color="red", ErrorExit=True, Exit=False)
        else:
            if isinstance(bw_master_password, str):
                if len(bw_master_password) < 8:
                    logger.pywarden_logger(Payload="BITWARDEN_MASTER_PASSWORD is not long enough, minimum length is 8", Color="red", ErrorExit=True, Exit=False)
                else:
                    global BITWARDEN_MASTER_PASSWORD
                    BITWARDEN_MASTER_PASSWORD = config['BITWARDEN_MASTER_PASSWORD']
            else:
                logger.pywarden_logger(Payload="BITWARDEN_MASTER_PASSWORD is not a string", Color="red", ErrorExit=True, Exit=False)

    bw_verbose = config['VERBOSITY']
    if config['VERBOSITY'] != None:
        if isinstance(bw_verbose, bool):
            global VERBOSITY
            VERBOSITY = config['VERBOSITY']
        else:
            logger.pywarden_logger(Payload="VERBOSITY is not a boolean", Color="red", ErrorExit=True, Exit=False)
    
    if config['PYWARDEN_ORG_ENABLED'] == True:

        bw_org_id = config['BITWARDEN_ORGANIZATION_ID']
        if config['BITWARDEN_ORGANIZATION_ID'] != None:
            if config['BITWARDEN_ORGANIZATION_ID'] == '':
                logger.pywarden_logger(Payload="BITWARDEN_ORGANIZATION_ID is not set", Color="red", ErrorExit=True, Exit=False)
            else:
                if isinstance(bw_org_id, str):
                    if len(bw_org_id) < 49:
                        logger.pywarden_logger(Payload="BITWARDEN_ORGANIZATION_ID is not long enough, minimum length is 49", Color="red", ErrorExit=True, Exit=False)
                    else:
                        global BITWARDEN_ORGANIZATION_ID
                        BITWARDEN_ORGANIZATION_ID = config['BITWARDEN_ORGANIZATION_ID']
                else:
                    logger.pywarden_logger(Payload="BITWARDEN_ORGANIZATION_ID is not a string", Color="red", ErrorExit=True, Exit=False)
    
        bw_org_secret = config['BITWARDEN_ORGANIZATION_SECRET']
        if config['BITWARDEN_ORGANIZATION_SECRET'] != None:
            if config['BITWARDEN_ORGANIZATION_SECRET'] == '':
                logger.pywarden_logger(Payload="BITWARDEN_ORGANIZATION_SECRET is not set", Color="red", ErrorExit=True, Exit=False)
            else:
                if isinstance(bw_org_secret, str):
                    if len(bw_org_secret) < 30:
                        logger.pywarden_logger(Payload="BITWARDEN_ORGANIZATION_SECRET is not long enough, minimum length is 30", Color="red", ErrorExit=True, Exit=False)
                    else:
                        global BITWARDEN_ORGANIZATION_SECRET
                        BITWARDEN_ORGANIZATION_SECRET = config['BITWARDEN_ORGANIZATION_SECRET']
                else:
                    if VERBOSITY == True:
                        logger.pywarden_logger(Payload="BITWARDEN_ORGANIZATION_SECRET is not a string", Color="red", ErrorExit=True, Exit=False)
                        print('BITWARDEN_ORGANIZATION_SECRET is not a string.')
                    exit(2)

        if VERBOSITY == True:
            if supress == False:
                logger.pywarden_logger(Payload="Pywarden is running in organization mode", Color="green", ErrorExit=False, Exit=False)
    else:
        if VERBOSITY == True:
            if supress == False:
                logger.pywarden_logger(Payload="Pywarden is running in personal mode", Color="green", ErrorExit=False, Exit=False)
        pass
    
    if VERBOSITY == True:
        if supress == False:
            logger.pywarden_logger(Payload="Pywarden Configuration parsed successfully", Color="green", ErrorExit=False, Exit=False)
    return(0)
