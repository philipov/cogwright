#!python
#-- setup.py -- cogwright

"""
"""

from setuptools import setup
from pathlib import Path
import os
os.environ['__SETUP_PY__'] = "cogwright"

#----------------------------------------------------------------------#

###
PROJECT_PATH = Path( '.' ).resolve( )
PROJECT_NAME = PROJECT_PATH.name

###
from cogwright import __version__

###
__description__ = "".join(list(open(str(PROJECT_PATH/'DESCRIPTION'))))


#----------------------------------------------------------------------#

###
setup(
    name            = PROJECT_NAME,
    packages        = [PROJECT_NAME],
    version         = __version__,

    description     = __description__,
    url             = 'https://github.com/philipov/cogwright',

    author          = 'Philip Loguinov',
    author_email    = 'philipov@gmail.com',

    entry_points={
        'console_scripts' : [ "".join([ 'cog', '=', PROJECT_NAME, '.__main__:main' ]) ],
    },

    requires = ['twine', 'wheel'],

    classifiers=[
        'Development Status : : 2 - Pre - Alpha',

        'Environment :: Console',
        'Environment :: Other Environment',

        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Customer Service',

        'License :: Other/Proprietary License',

        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.6',
    ],
)


#----------------------------------------------------------------------#
