from pelican_jupyter import markup as nb_markup


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
MEDIUS_CATEGORIES = []
MEDIUS_AUTHORS = []

TYPOGRIFY = True

DEFAULT_LANG = 'en'
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = "%Y.%m.%d"
DEFAULT_CATEGORY = "Other"
SUMMARY_MAX_LENGTH = 40

PATH = 'content'
STATIC_PATHS = ['assets']

DELETE_OUTPUT_DIRECTORY = True

MARKUP = ("md", "ipynb")
IPYNB_MARKUP_USE_FIRST_CELL = True

PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]