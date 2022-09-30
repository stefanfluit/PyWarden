#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import os
from pathlib import Path


def get_conf_file():
    pywarden_config_template = "https://raw.githubusercontent.com/stefanfluit/PyWarden/main/pywarden_config_template.yaml"
    pywarden_conf_opt = "/opt/pywarden/pywarden_config.yaml"

    # Check if bw_auth_endpoint is set
    current_unix_user = os.getlogin()

    # Format string of current user home directory
    current_unix_user_home = "/home/" + current_unix_user + "/" + "pywarden_config.yaml"

    # Fetch the template from github, if it does not exist yet in home or /opt
    if not os.path.exists(current_unix_user_home):
        if not os.path.exists(pywarden_conf_opt):
            urllib.request.urlretrieve(pywarden_config_template, current_unix_user_home)
            return Path(current_unix_user_home)
        else:
            return Path(pywarden_conf_opt)

    return Path(current_unix_user_home)
