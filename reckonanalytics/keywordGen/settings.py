import os

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

...

MEDIA_ROOT = PROJECT_PATH + '/media/'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)
