#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from pywarden.api import token
from pywarden.pywarden import handle_config

def get_group_id(group_name):
    BW_BEARER_TOKEN = token.get_bearer_token()
    headers = {
    'Authorization': 'Bearer {}'.format(BW_BEARER_TOKEN),
    }
    response = requests.get(handle_config.BITWARDEN_PUBLIC_API_URL + '/public/groups', headers=headers)
    for group in response.json()['data']:
        if group['name'] == group_name:
            return(group['id'])
