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

ISO2COUNTRIES=({
    'AF': 'Afghanistan',
    'AX': 'Aland Islands',
    'AL': 'Albania',
    'DZ': 'Algeria',
    'AS': 'American Samoa',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    'AQ': 'Antarctica',
    'AG': 'Antigua and Barbuda',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AW': 'Aruba',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BS': 'Bahamas the',
    'BH': 'Bahrain',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Belarus',
    'BE': 'Belgium',
    'BZ': 'Belize',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BT': 'Bhutan',
    'BO': 'Bolivia',
    'BA': 'Bosnia and Herzegovina',
    'BW': 'Botswana',
    'BV': 'Bouvet Island (Bouvetoya)',
    'BR': 'Brazil',
    'IO': 'British Indian Ocean Territory (Chagos Archipelago)',
    'VG': 'British Virgin Islands',
    'BN': 'Brunei Darussalam',
    'BG': 'Bulgaria',
    'BF': 'Burkina Faso',
    'BI': 'Burundi',
    'KH': 'Cambodia',
    'CM': 'Cameroon',
    'CA': 'Canada',
    'CV': 'Cape Verde',
    'KY': 'Cayman Islands',
    'CF': 'Central African Republic',
    'TD': 'Chad',
    'CL': 'Chile',
    'CN': 'China',
    'CX': 'Christmas Island',
    'CC': 'Cocos (Keeling) Islands',
    'CO': 'Colombia',
    'KM': 'Comoros the',
    'CD': 'Congo',
    'CG': 'Congo the',
    'CK': 'Cook Islands',
    'CR': 'Costa Rica',
    'CI': 'Cote d\'Ivoire',
    'HR': 'Croatia',
    'CU': 'Cuba',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DK': 'Denmark',
    'DJ': 'Djibouti',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'EC': 'Ecuador',
    'EG': 'Egypt',
    'SV': 'El Salvador',
    'GQ': 'Equatorial Guinea',
    'ER': 'Eritrea',
    'EE': 'Estonia',
    'ET': 'Ethiopia',
    'FO': 'Faroe Islands',
    'FK': 'Falkland Islands (Malvinas)',
    'FJ': 'Fiji the Fiji Islands',
    'FI': 'Finland',
    'FR': 'France, French Republic',
    'GF': 'French Guiana',
    'PF': 'French Polynesia',
    'TF': 'French Southern Territories',
    'GA': 'Gabon',
    'GM': 'Gambia the',
    'GE': 'Georgia',
    'DE': 'Germany',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GR': 'Greece',
    'GL': 'Greenland',
    'GD': 'Grenada',
    'GP': 'Guadeloupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GG': 'Guernsey',
    'GN': 'Guinea',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HT': 'Haiti',
    'HM': 'Heard Island and McDonald Islands',
    'VA': 'Holy See (Vatican City State)',
    'HN': 'Honduras',
    'HK': 'Hong Kong',
    'HU': 'Hungary',
    'IS': 'Iceland',
    'IN': 'India',
    'ID': 'Indonesia',
    'IR': 'Iran',
    'IQ': 'Iraq',
    'IE': 'Ireland',
    'IM': 'Isle of Man',
    'IL': 'Israel',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JP': 'Japan',
    'JE': 'Jersey',
    'JO': 'Jordan',
    'KZ': 'Kazakhstan',
    'KE': 'Kenya',
    'KI': 'Kiribati',
    'KP': 'Korea',
    'KR': 'Korea',
    'KW': 'Kuwait',
    'KG': 'Kyrgyz Republic',
    'LA': 'Lao',
    'LV': 'Latvia',
    'LB': 'Lebanon',
    'LS': 'Lesotho',
    'LR': 'Liberia',
    'LY': 'Libyan Arab Jamahiriya',
    'LI': 'Liechtenstein',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MO': 'Macao',
    'MK': 'Macedonia',
    'MG': 'Madagascar',
    'MW': 'Malawi',
    'MY': 'Malaysia',
    'MV': 'Maldives',
    'ML': 'Mali',
    'MT': 'Malta',
    'MH': 'Marshall Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MU': 'Mauritius',
    'YT': 'Mayotte',
    'MX': 'Mexico',
    'FM': 'Micronesia',
    'MD': 'Moldova',
    'MC': 'Monaco',
    'MN': 'Mongolia',
    'ME': 'Montenegro',
    'MS': 'Montserrat',
    'MA': 'Morocco',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibia',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'AN': 'Netherlands Antilles',
    'NL': 'Netherlands the',
    'NC': 'New Caledonia',
    'NZ': 'New Zealand',
    'NI': 'Nicaragua',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Norfolk Island',
    'MP': 'Northern Mariana Islands',
    'NO': 'Norway',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PW': 'Palau',
    'PS': 'Palestinian Territory',
    'PA': 'Panama',
    'PG': 'Papua New Guinea',
    'PY': 'Paraguay',
    'PE': 'Peru',
    'PH': 'Philippines',
    'PN': 'Pitcairn Islands',
    'PL': 'Poland',
    'PT': 'Portugal, Portuguese Republic',
    'PR': 'Puerto Rico',
    'QA': 'Qatar',
    'RE': 'Reunion',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'BL': 'Saint Barthelemy',
    'SH': 'Saint Helena',
    'KN': 'Saint Kitts and Nevis',
    'LC': 'Saint Lucia',
    'MF': 'Saint Martin',
    'PM': 'Saint Pierre and Miquelon',
    'VC': 'Saint Vincent and the Grenadines',
    'WS': 'Samoa',
    'SM': 'San Marino',
    'ST': 'Sao Tome and Principe',
    'SA': 'Saudi Arabia',
    'SN': 'Senegal',
    'RS': 'Serbia',
    'SC': 'Seychelles',
    'SL': 'Sierra Leone',
    'SG': 'Singapore',
    'SK': 'Slovakia (Slovak Republic)',
    'SI': 'Slovenia',
    'SB': 'Solomon Islands',
    'SO': 'Somalia, Somali Republic',
    'ZA': 'South Africa',
    'GS': 'South Georgia and the South Sandwich Islands',
    'ES': 'Spain',
    'LK': 'Sri Lanka',
    'SD': 'Sudan',
    'SR': 'Suriname',
    'SJ': 'Svalbard & Jan Mayen Islands',
    'SZ': 'Swaziland',
    'SE': 'Sweden',
    'CH': 'Switzerland, Swiss Confederation',
    'SY': 'Syrian Arab Republic',
    'TW': 'Taiwan',
    'TJ': 'Tajikistan',
    'TZ': 'Tanzania',
    'TH': 'Thailand',
    'TL': 'Timor-Leste',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad and Tobago',
    'TN': 'Tunisia',
    'TR': 'Turkey',
    'TM': 'Turkmenistan',
    'TC': 'Turks and Caicos Islands',
    'TV': 'Tuvalu',
    'UG': 'Uganda',
    'UA': 'Ukraine',
    'AE': 'United Arab Emirates',
    'GB': 'United Kingdom',
    'US': 'United States of America',
    'UM': 'United States Minor Outlying Islands',
    'VI': 'United States Virgin Islands',
    'UY': 'Uruguay, Eastern Republic of',
    'UZ': 'Uzbekistan',
    'VU': 'Vanuatu',
    'VE': 'Venezuela',
    'VN': 'Vietnam',
    'WF': 'Wallis and Futuna',
    'EH': 'Western Sahara',
    'YE': 'Yemen',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe'
})

def isocode_to_country(code):
    return ISO2COUNTRIES[code]

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
