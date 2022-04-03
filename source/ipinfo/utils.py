# -*- coding: utf-8 -*-
"""Helper Functions"""
import json
import re

from .exceptions import ApiError, ApiTokenError, UnknownPythonError

IPINFO_ENDPOINT_1 = (
    "https://ipinfo.io/json" "?token={}"
)
IPINFO_ENDPOINT_2 = (
    "https://ipinfo.io/{}/json" "?token={}"
)

# Make a regular expression for validating an Ip-address
RE_VALID_IP = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def init_workflow(workflow):
    """Run operation to get workflow ready

    Inject config into Workflow

    Arguments:
        workflow {workflow.Workflow3} -- The workflow object

    Returns:
        workflow -- the passed in workflow object
    """
    from .config import Config

    workflow.config = Config()
    return workflow

def valid_ip(ipaddress=""):
    return re.search(RE_VALID_IP, ipaddress)
        
def get_ipdata(config, ipaddress=""):
    """Fetch the ip data for the specfcified ip

    Arguments:
        config -- Config object

    Keyword Arguments:
        ipaddress {str} -- ip address to lookup, empty string to use actual 
                      (default: {""})

    Returns:
        dict -- fetched ip data

    Raises:
        AppIDError -- Raised when App ID can not be used
        ApiError -- Raised when API is unreachable or return bad response
        UnknownPythonError -- Raised when Python runtime version can not be
                              correctly detected
    """
    from urllib import error, request

    # Initiliase the response
    ipdata = []
    
    try:
        if not ipaddress:
            response = request.urlopen(IPINFO_ENDPOINT_1.format(config.apitoken))
            ipdata = json.load(response)
        else:
            if valid_ip(ipaddress):
                response = request.urlopen(IPINFO_ENDPOINT_2.format(ipaddress,config.apitoken))
                ipdata = json.load(response)
    except error.HTTPError as err:
        response = json.load(err)
        if err.code == 401:
            raise ApiTokenError(
                "Invalid API token: {}".format(config.apitoken), response["description"]
            )
        elif err.code == 429:
            raise ApiTokenError("Access Restricted", response["description"])
        else:
            raise ApiError("Unexpected Error", response["description"])
    return ipdata
