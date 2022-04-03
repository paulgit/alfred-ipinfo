# -*- coding: utf-8 -*-
"""Exceptions used in this module"""


class IPInfoError(Exception):
    """Base Class used to declare other errors for Coinc

    Extends:
        Exception
    """
    pass


class ConfigError(IPInfoError):
    """Raised when there are invalid value filled in Configuration Sheet

    Extends:
        IPInfoError
    """
    pass

class ApiTokenError(IPInfoError):
    """Raised when App Token can not be used

    Extends:
        IPInfoError
    """
    pass


class ApiError(IPInfoError):
    """Raised when API is unreachable or return bad response

    Extends:
        IPInfoError
    """
    pass


class UnknownPythonError(IPInfoError):
    """Raised when Python runtime version can not be correctly detacted

    Extends:
        IPInfoError
    """
    pass
