#!python
#-- __main.py

"""
unit tests
"""

from pathlib import Path
import pytest

#----------------------------------------------------------------------#


import shlex
import pytest

#----------------------------------------------------------------------#

from cogwright.__main__ import cog
from cogwright.__main__ import command_line_parameters

params_argv = list( )
params_argv.append( shlex.split( 'extract' ) )

@pytest.mark.parametrize( "argv", params_argv )
def test__main( argv, path_testdata ) :
    import os

    os.chdir( str( path_testdata ) )
    args = command_line_parameters( argv )
    cog( args )

    # assert False


#----------------------------------------------------------------------#
