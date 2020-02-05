#!/usr/bin/env python3

import os
import requests

CONFIG = """
# This file is autogenerated from update.py, don't touch
# Modify update.py instead

baseURL = "https://aflplus.plus/"
languageCode = "en-us"
title = "AFLplusplus"
publishDir = "docs"

[params]
  sitename = "AFLplusplus"
  description = "The AFLplusplus website"
  image = "ogimage.png"
  ogimage = "ogimage.png"
  BookMenuBundle = "/menu"
  BookLogo = 'logo_256x256.png'
  ReleaseName = "__REL_NAME__"
  ReleaseURL = "__REL_URL__"
"""

os.system("cd AFLplusplus && git pull")
os.system("cp -v AFLplusplus/docs/*.md content/docs/")

r = requests.get("https://api.github.com/repos/vanhauser-thc/AFLplusplus/releases/latest")

CONFIG = CONFIG.replace("__REL_NAME__", r.json()["name"])
CONFIG = CONFIG.replace("__REL_URL__", r.json()["html_url"])

with open("config.toml", "w") as f:
    f.write(CONFIG)

