#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
import subprocess
from pywarden.pywarden import handle_config

def gen_config():
    dir = handle_config.get_dir(cut=True)

    # Be sure that there are no config files in the project dir or home dir
    if os.path.isfile(dir + '/' + 'pywarden_config.yml'):
        print('pywarden_config.yml already exists in the project dir')
        exit(2)
    if os.path.isfile(os.path.expanduser('~') + '/pywarden_config.yml'):
        print('pywarden_config.yml already exists in the home dir')
        exit(2)

    # Check for the existense of the template file in the project dir
    valid_config_template_name = 'pywarden_config_template.yaml'
    if os.path.isfile(dir + '/' + valid_config_template_name):
        subprocess.run(['cp', dir + '/' + valid_config_template_name, dir + '/' + 'pywarden_config.yaml'])
        print('Copied template config file to project dir')
        config_file = dir + '/' + 'pywarden_config.yaml'
    
    # Edit the empty variables
    with open(config_file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
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
    print('Config file created')
