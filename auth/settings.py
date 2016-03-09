# -*- coding: utf-8 -*-

"""Default options for the application.
"""

# version
VERSION = '0.2'

# sqlite DB file
SQLITE_DB = 'db/auth.db' 

# maximum number of authorized IPs per user 
MAX_AUTH_IP_COUNT = 255

# automatic IP authorization without authentication
# do not set this to True, unless you *really* know what you are doing
AUTO_AUTH = False

# web debug output dump
DEBUG = False