#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import configparser

def pywarden_version():
    fetch_url = "https://raw.githubusercontent.com/stefanfluit/PyWarden/main/setup.cfg"
    with open ("setup.cfg", "w") as f:
        f.write(requests.get(fetch_url).text)
    config = configparser.ConfigParser()
    config.read("setup.cfg")
    return config["metadata"]["version"]
