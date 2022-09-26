#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from pywarden.classes import classes
from pywarden.pywarden import version

def pywarden_logger(Payload=None, Color=None, Prefix="PyWarden ", ErrorExit=None, Exit=None):
    Payload     = str(Payload)
    Color       = str(Color)
    Prefix      = str(Prefix)
    Exit        = bool(Exit)
    ErrorExit   = bool(ErrorExit)

    pywarden_version = version.pywarden_version()

    if Color == "red":
        print("\033[91m" + Prefix + pywarden_version + ":" + " " + Payload + "\033[0m")
        if ErrorExit == True:
            exit(1)
        if Exit == True:
            exit(0)
    elif Color == "green":
        print("\033[92m" + Prefix + pywarden_version + ":" + " " + Payload + "\033[0m")
        if ErrorExit == True:
            exit(1)
        if Exit == True:
            exit(0)
    elif Color == "blue":
        print("\033[94m" + Prefix + pywarden_version + ":" + " " + Payload + "\033[0m")
        if ErrorExit == True:
            exit(1)
        if Exit == True:
            exit(0)
