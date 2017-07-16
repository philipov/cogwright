
'''
'''

from pathlib import Path

#----------------------------------------------------------------------#

payload_filename_win    = ""
payload_filename_nix    = ""

extract_tmp_suffix      = Path( 'a') / 'a_b'
extract_suffix          = Path('a') / 'ab'



def write_version_file( payload_path:Path ) -> str:
    with open( str( payload_path / 'ReleaseNotes.txt' ) ) as file :
        for line in file :
            if line.startswith( "VERSION_" ) :
                version = line.strip( ).split( "VERSION_" )[-1]
                with open( str( payload_path / '__version__.py' ), 'w' ) as version_file :
                    version_string = "__version__ = '" + version + "'"
                    print( version_string, file=version_file, flush=True )
                break
    return version

#----------------------------------------------------------------------#
