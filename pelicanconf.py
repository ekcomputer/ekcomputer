AUTHOR = 'Ethan Kyzivat'
SITENAME = 'Ethan D. Kyzivat, PhD candidate'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
OUTPUT_PATH = 'docs'
THEME = 'themes/backdrop'
TIMEZONE = 'US/Eastern'
IGNORE_FILES = ['post-templates.*']
DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'Articles'
DELETE_OUTPUT_DIRECTORY = True # should be False by default

# for backdrop theme
# PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PAGINATED_TEMPLATES = {'category': None, 'author': None, 'archives': None}
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PROFILE_IMAGE = "images/Snapchat-505899047.jpg"
BACKDROP_IMAGE = 'images/DJI_0182-crop1.png'

# auto-naming articles or pages
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
# SITEURL
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DISPLAY_PAGES_ON_MENU = True

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
RELATIVE_URLS = True # should be false for publishing, or make sure I understand what it means...
