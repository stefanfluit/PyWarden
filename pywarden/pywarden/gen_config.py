#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml
import getpass

from pywarden.logger import logger
from pywarden.pywarden import conf_file

def gen_config():

    config_file = conf_file.get_conf_file()

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
        PASSWD_STRING = "PASSWORD"
        SECRET_STRING = "SECRET"
        if PASSWD_STRING in variable:
            prompt = "Please enter a value for " + variable + ": "
            config[variable] = getpass.getpass(prompt=prompt, stream=None)
        elif SECRET_STRING in variable:
            prompt = "Please enter a value for " + variable + ": "
            config[variable] = getpass.getpass(prompt=prompt, stream=None)
        else:
            config[variable] = input('Please enter a value for ' + variable + ": ")
        
    with open(config_file, 'w') as file:
        documents = yaml.dump(config, file)
