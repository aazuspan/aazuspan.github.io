AUTHOR = 'Aaron Zuspan'
SITENAME = 'Aaron Zuspan'


TIMEZONE = 'America/Los_Angeles'


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

THEME = './theme/medius/'

TYPOGRIFY = True

DEFAULT_LANG = 'en'
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%Y.%m.%d"
DEFAULT_CATEGORY = "Other"
SUMMARY_MAX_LENGTH = 40

PATH = 'content'
STATIC_PATHS = ['assets']

DELETE_OUTPUT_DIRECTORY = True