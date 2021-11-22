#!/usr/bin/env python
# coding=utf-8
# -*- coding:utf-8 -*-

import os
from urllib import request
try:
    import yaml
except:
    os.system("pip3 install pyyaml")
    import yaml

yaml_path = "https://raw.githubusercontent.com/iceveil/py3-package-names/master/package-names.yaml"

def get_package(name):
    try:
        response = request.urlopen(yaml_path)
    except:
        return False
    
    data = yaml.load(response, Loader=yaml.BaseLoader)
    
    try:
        package_name = data[name]
    except:
        package_name = None

    return package_name
