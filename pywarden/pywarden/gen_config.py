#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.log import error
import yaml
from pathlib import Path
import urllib.request
import os

from pywarden.logger import logger

def gen_config():
    pywarden_config_template = "https://raw.githubusercontent.com/stefanfluit/PyWarden/main/pywarden_config_template.yaml"

    # Check if bw_auth_endpoint is set
    current_unix_user = os.getlogin()
    # Format string of current user home directory
    current_unix_user_home = "/home/" + current_unix_user + "/" + "pywarden_config.yaml"
    # Fetch the template from github, if it does not exist yet
    if not os.path.isfile(current_unix_user_home):
        urllib.request.urlretrieve(pywarden_config_template, current_unix_user_home)
    config_file = Path(current_unix_user_home)

    with open(config_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            error_message = "Error while loading the config file: " + exc
            logger.pywarden_logger(Payload=error_message, Color="red")

    # Fill a list of all the variables that need to be filled
    variables = []
    for key, value in config.items():
        if value == '':
            variables.append(key)

    # Ask the user for input for every variable
    for variable in variables:
        config[variable] = input('Please enter a value for ' + variable + ': ')

    # Write the config file
    with open(config_file, 'w') as file:
        documents = yaml.dump(config, file)
