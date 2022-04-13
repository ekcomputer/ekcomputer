AUTHOR = 'Ethan Kyzivat'
SITENAME = 'Ethan D. Kyzivat, PhD candidate'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'
THEME = 'themes/backdrop'
TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# for backdrop theme
# PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PAGINATED_TEMPLATES = {'category': None, 'author': None, 'archives': None}
PROFILE_IMAGE = "./content/images/Snapchat-505899047.jpg"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Twitter', 'https://www.twitter.com/ethankyzivat'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
