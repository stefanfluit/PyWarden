#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def gen_password(PASSWORD_LENGTH=8):
    gen_password = subprocess.check_output(f'bw generate --uppercase --lowercase --number --special --length {PASSWORD_LENGTH}', shell=True, encoding='utf-8')
    return(gen_password)
