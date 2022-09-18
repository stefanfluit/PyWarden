#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path
import validators
import subprocess

def get_dir(cut=True):
    if cut == False:
        pywarden_dir = subprocess.run(['pwd'], stdout=subprocess.PIPE)
        pywarden_dir = pywarden_dir.stdout.decode('utf-8').strip()
        return(pywarden_dir)
    if cut == True:
        pywarden_dir = subprocess.run(['pwd'], stdout=subprocess.PIPE)
        pywarden_dir = pywarden_dir.stdout.decode('utf-8').strip()
        p = Path(pywarden_dir)
        str(p.parent)
        p_parts = list(p.parts)
        p_parts.pop()
        p_parts.pop()
        p_parts = '/'.join(p_parts)
        p_parts = p_parts[1:]
        return(p_parts)

def manage_configuration(supress=False):
    pywarden_dir = get_dir(cut=False)

    valid_config_name = 'pywarden_config.yaml'

    p = Path(pywarden_dir)
    str(p.parent)
    p_parts = list(p.parts)
    p_parts.pop()
    p_parts.pop()
    p_parts = '/'.join(p_parts)
    p_parts = p_parts[1:]

    pywarden_config = p_parts + '/' + valid_config_name
    pytwarden_home_config = os.path.expanduser('~') + '/' + valid_config_name

    if os.path.isfile(pywarden_config):
        with open(pywarden_config, "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
    else:
        if os.path.isfile(pytwarden_home_config):
            with open(pytwarden_home_config, "r") as stream:
                try:
                    config = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            print("No configuration file found. Please create one in your home directory or in the project directory.")

    bw_passwd_length = config['BITWARDEN_PASSWORD_LENGTH']
    if isinstance(bw_passwd_length, int):
        if config['BITWARDEN_PASSWORD_LENGTH'] < 8:
            print('BITWARDEN_PASSWORD_LENGTH is not long enough, minumum length is 8')
            exit(2)
        else:
            global BITWARDEN_PASSWORD_LENGTH
            BITWARDEN_PASSWORD_LENGTH = int(config['BITWARDEN_PASSWORD_LENGTH'])
    else:
        print('BITWARDEN_PASSWORD_LENGTH is not an integer, you dont need to quote it.')
        exit(2)

    bw_url = config['BITWARDEN_SERVER_URL']
    if config['BITWARDEN_SERVER_URL'] != None:
        if validators.url(bw_url):
            global BITWARDEN_URL
            BITWARDEN_URL = config['BITWARDEN_SERVER_URL']
        else:
            print('BITWARDEN_URL is not a valid URL')
            exit(2)
    else:
        print('BITWARDEN_SERVER_URL is not set')
        exit(2)

    bw_public_api_url = config['BITWARDEN_PUBLIC_API_URL']
    if config['BITWARDEN_PUBLIC_API_URL'] != None:
        if validators.url(bw_public_api_url):
            global BITWARDEN_PUBLIC_API_URL
            BITWARDEN_PUBLIC_API_URL = config['BITWARDEN_PUBLIC_API_URL']
        else:
            print('BITWARDEN_PUBLIC_API_URL is not a valid URL')
            exit(2)
    else:
        print('BITWARDEN_PUBLIC_API_URL is not set')
        exit(2)

    bw_auth_endpoint = config['BITWARDEN_AUTH_ENDPOINT']
    if config['BITWARDEN_AUTH_ENDPOINT'] != None:
        if validators.url(bw_auth_endpoint):
            global BITWARDEN_AUTH_ENDPOINT
            BITWARDEN_AUTH_ENDPOINT = config['BITWARDEN_AUTH_ENDPOINT']
        else:
            print('BITWARDEN_AUTH_ENDPOINT is not a valid URL')
            exit(2)
    else:
        print('BITWARDEN_AUTH_ENDPOINT is not set')
        exit(2)
    
    bw_client_id = config['BITWARDEN_API_CLIENT_ID']
    if config['BITWARDEN_API_CLIENT_ID'] != None:
        if config['BITWARDEN_API_CLIENT_ID'] == '':
            print('BITWARDEN_API_CLIENT_ID is not set')
            exit(2)
        else:
            if isinstance(bw_client_id, str):
                if len(bw_client_id) < 41:
                    print('BITWARDEN_API_CLIENT_ID is not long enough, minumum length is 40')
                    exit(2)
                else:
                    global BITWARDEN_API_CLIENT_ID
                    BITWARDEN_API_CLIENT_ID = config['BITWARDEN_API_CLIENT_ID']
            else:
                print('BITWARDEN_API_CLIENT_ID is not a string.')
                exit(2)
    else:
        print('BITWARDEN_API_CLIENT_ID is not set')
        exit(2)
    
    bw_client_secret = config['BITWARDEN_API_CLIENT_SECRET']
    if config['BITWARDEN_API_CLIENT_SECRET'] != None:
        if config['BITWARDEN_API_CLIENT_SECRET'] == '':
            print('BITWARDEN_API_CLIENT_SECRET is not set')
            exit(2)
        else:
            if isinstance(bw_client_secret, str):
                if len(bw_client_secret) < 30:
                    print('BITWARDEN_API_CLIENT_SECRET is not long enough, minumum length is 30')
                    exit(2)
                else:
                    global BITWARDEN_API_CLIENT_SECRET
                    BITWARDEN_API_CLIENT_SECRET = config['BITWARDEN_API_CLIENT_SECRET']
            else:
                print('BITWARDEN_API_CLIENT_SECRET is not a string.')
                exit(2)
    
    bw_master_password = config['BITWARDEN_MASTER_PASSWORD']
    if config['BITWARDEN_MASTER_PASSWORD'] != None:
        if config['BITWARDEN_MASTER_PASSWORD'] == '':
            print('BITWARDEN_MASTER_PASSWORD is not set')
            exit(2)
        else:
            if isinstance(bw_master_password, str):
                if len(bw_master_password) < 8:
                    print('BITWARDEN_MASTER_PASSWORD is not long enough, minumum length is 8')
                    exit(2)
                else:
                    global BITWARDEN_MASTER_PASSWORD
                    BITWARDEN_MASTER_PASSWORD = config['BITWARDEN_MASTER_PASSWORD']
            else:
                print('BITWARDEN_MASTER_PASSWORD is not a string.')
                exit(2)

    bw_verbose = config['VERBOSITY']
    if config['VERBOSITY'] != None:
        if isinstance(bw_verbose, bool):
            global VERBOSITY
            VERBOSITY = config['VERBOSITY']
        else:
            print('VERBOSITY is not a boolean')
            exit(2)
    
    if config['PYWARDEN_ORG_ENABLED'] == True:

        bw_org_id = config['BITWARDEN_ORGANIZATION_ID']
        if config['BITWARDEN_ORGANIZATION_ID'] != None:
            if config['BITWARDEN_ORGANIZATION_ID'] == '':
                print('BITWARDEN_ORGANIZATION_ID is not set')
                exit(2)
            else:
                if isinstance(bw_org_id, str):
                    if len(bw_org_id) < 49:
                        print('BITWARDEN_ORGANIZATION_ID is not long enough, minumum length is 49')
                        exit(2)
                    else:
                        global BITWARDEN_ORGANIZATION_ID
                        BITWARDEN_ORGANIZATION_ID = config['BITWARDEN_ORGANIZATION_ID']
                else:
                    print('BITWARDEN_ORGANIZATION_ID is not a string.')
                    exit(2)
    
        bw_org_secret = config['BITWARDEN_ORGANIZATION_SECRET']
        if config['BITWARDEN_ORGANIZATION_SECRET'] != None:
            if config['BITWARDEN_ORGANIZATION_SECRET'] == '':
                print('BITWARDEN_ORGANIZATION_SECRET is not set')
                exit(2)
            else:
                if isinstance(bw_org_secret, str):
                    if len(bw_org_secret) < 30:
                        print('BITWARDEN_ORGANIZATION_SECRET is not long enough, minumum length is 30')
                        exit(2)
                    else:
                        global BITWARDEN_ORGANIZATION_SECRET
                        BITWARDEN_ORGANIZATION_SECRET = config['BITWARDEN_ORGANIZATION_SECRET']
                else:
                    if VERBOSITY == True:
                        print('BITWARDEN_ORGANIZATION_SECRET is not a string.')
                    exit(2)

        if VERBOSITY == True:
            if supress == False:
                print('Organization settings parsed successfully.')
    else:
        if VERBOSITY == True:
            if supress == False:
                print('Organization is not enabled, skipping..')
        pass
    
    if VERBOSITY == True:
        if supress == False:
            print('Configuration parsed successfully.')
    return(0)
