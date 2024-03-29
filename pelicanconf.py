from __future__ import unicode_literals

AUTHOR = u'Chulpyo'
SITENAME = u'D-E-V-L-O-G'
SITESUBTITLE = u'개발로그'
SITEURL = ''

PATH = 'content'

DEFAULT_DATE = 'fs'

DEFAULT_DATE_FORMAT = '%Y/%m/%d'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = u'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/arulraj.net'),
          ('Twitter', 'http://twitter.com/arulrajnet')
          )

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets']
PAGE_PATHS = ['pages']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/favicon.png': {'path': 'favicon.png'},
    'assets/CNAME': {'path': 'CNAME'}
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

### Plugins

PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Comments
# DISQUS_SITENAME = "attilademo"

# Analytics
# GOOGLE_ANALYTICS = "UA-3546274-12"

THEME = 'chulpyome'

### Theme specific settings

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COVER and use cover in individual articles.
# HEADER_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

# This is deprecated. Will be removed in future releases.
# Work around will be use HOME_COLOR and use color in individual articles.
# HEADER_COLOR = 'black'

# To set background image for the home page.
HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

# Custom Header

HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}

AUTHORS_BIO = {

  "chulpyo": {
    "name": "Chulpyo Kim",
    "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    "image": "assets/images/avatar.png",
    "website": "https://blog.chulpyo.me",
    "linkedin": "unavailable",
    "github": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }

}

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']


# Output