# -*- coding: utf-8 -*-
"""Functions to be called by workflow"""

from ipaddress import ip_address
from .exceptions import IPInfoError, ConfigError
from .utils import (
    init_workflow,
    get_ipdata,
)

__all__ = [
    "lookup_ipinfo",
    "my_ipinfo",
    "help_me",
]

def load(workflow):
    workflow.send_feedback()

def my_ipinfo(workflow):
    """Fetch IP data for the current IP address"""
    fetch_ipinfo(workflow,"")

def lookup_ipinfo(workflow):
    """Fetch IP data for the passed IP address"""
    fetch_ipinfo(workflow,workflow.args[1:][0])

def fetch_ipinfo(workflow,ipaddress=""):
    """Fetch IP data and return Alfred item"""
    try:
        init_workflow(workflow)
        
        ipdata = get_ipdata(workflow.config,ipaddress)
        
        if len(ipdata) > 0:
            argvalue=ipdata["ip"]
            if ip_address:
                argvalue+=" (" + ipdata["city"] + ", " + ipdata["region"] + ", " + ipdata["country"] + " • " + ipdata["org"] + ")"

            workflow.add_item(
                title=ipdata["ip"],
                subtitle=ipdata["city"] + ", " + ipdata["region"] + ", " + ipdata["country"] + " • " + ipdata["org"],
                valid=True,
                arg=argvalue,
                icon=str.format("./images/{}_64.png",ipdata["country"].lower())
        )
    except IPInfoError as error:
        workflow.logger.info("ipinfo: {}".format(type(error).__name__))
        workflow.logger.info(error)
        workflow.add_item(
            title=error.args[0], subtitle=error.args[1], icon="./images/cancel.png"
        )
    # except Exception as error:
    #     workflow.logger.info("Python: {}".format(type(error).__name__))
    #     workflow.logger.info(error)
    #     workflow.add_item(title="Python Error: {}".format(type(error).__name__),
    #                       subtitle=error.args[0],
    #                       icon="hints/cancel.png")1.1.1.11.1.1.11.1.1.1(Los Angeles, California, US • AS13335 Cloudflare, Inc.)
    workflow.send_feedback()

def help_me(workflow):
    """Function for showing example usage"""
    workflow.add_item(
        title="ipinfo",
        subtitle="Fetch the IP information for your current internet IP address",
        valid=True,
        arg="ipinfo",
    )
    workflow.add_item(
        title="iplookup 1.1.1.1",
        subtitle="Fetch the IP information for the specified internet IP address",
        valid=True,
        arg="iplookup 1.1.1.1",
    )
    workflow.add_item(
        title="Documentation",
        subtitle="Select this to find out more comprehensive documentation",
        icon="./images/info.png",
        valid=True,
        arg="ipinfo workflow:help",
    )
    workflow.send_feedback()
