# -*- coding: utf-8 -*-
"""Helper class for loading config set in Alfred Variable Sheet"""
import os
from .exceptions import ConfigError

class Config():
    """Helper class for loading config set in Alfred Environment Variables Sheet

    Raises:
        ConfigError -- Raised when there are invalid value
                       filled in Configuration Sheet
    """
    def __init__(self):
        # APITOKEN
        apitoken = os.getenv("APITOKEN")
        if not apitoken:
            raise ConfigError("Please setup your ipinfo.io APITOKEN to use this workflow",
                              ("Paste your api token into workflow environment"
                               "variables sheet in Alfred Preferences"))
        self.apitoken = apitoken
