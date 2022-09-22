#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from pywarden.pywarden import handle_config

def get_bearer_token():
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = 'grant_type=client_credentials&scope=api.organization&client_id={}&client_secret={}'.format(handle_config.BITWARDEN_ORGANIZATION_ID, handle_config.BITWARDEN_ORGANIZATION_SECRET)
    response = requests.post(handle_config.BITWARDEN_AUTH_ENDPOINT, headers=headers, data=data)
    return response.json()['access_token']
