AUTHOR = 'Aaron Zuspan'
SITENAME = 'Longitudes and Platitudes'
# SITEURL = 'https://aazuspan.github.io'
SITEURL = ''


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

READERS = {'html': None}

SOCIAL = (('twitter', 'https://twitter.com/aazuspan'),
          ('github', 'https://github.com/aazuspan'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './theme/medius/'

DEFAULT_DATE_FORMAT = "%b %d, %Y"                 # short date format, optional but recommended 
USER_LOGO_URL = "http://i.imgur.com/zzCRZUH.jpg"  # change URL to point to desired logo for site

COLOR_SCHEME_CSS = 'darkly.css'
HEADER_COLOR = 'red'

PATH = 'content'
STATIC_PATHS = ['assets']

DELETE_OUTPUT_DIRECTORY = True