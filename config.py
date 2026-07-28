#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8630903419:AAHA9pXG6bKBMBwgY9Ee9O4UckpuJoz1Rao")
    API_ID = int(os.environ.get("API_ID", "8630903419"))
    API_HASH = os.environ.get("API_HASH", "AAHA9pXG6bKBMBwgY9Ee9O4UckpuJoz1Rao")
    AUTH_USERS = "1411895712"

