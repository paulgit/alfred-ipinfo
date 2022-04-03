# -*- coding: utf-8 -*-
"""Script for Default keyword"""
import sys
import ipinfo
from workflow import Workflow3
from workflow.util import reload_workflow


def main(workflow):
    """The main workflow entry function"""
    method = str(workflow.args.pop(0))
    if method in ipinfo.__all__:
        workflow.run(getattr(ipinfo, method))
    else:
        workflow.run(ipinfo.help_me)


if __name__ == "__main__":
    WF = Workflow3(
        update_settings={
            "github_slug": "paulgit/alfred-ipinfo",
            "frequency": 7
        },
        help_url="https://github.com/paulgit/alfred-ipinfo")
    sys.exit(WF.run(main))
