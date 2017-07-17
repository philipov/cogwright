
'''
'''

from pathlib import Path

#----------------------------------------------------------------------#

url_ftp                 = "ftp.application.com"

payload_filename_win    = "archivename_windows.zip"
payload_filename_nix    = "archivename_linux.tar.gz"

extract_tmp_suffix      = Path( 'company' ) / 'application'
extract_suffix          = Path( 'company' ) / 'core'

path_source             = Path(__file__).parents[0] / 'module'
path_payload            = path_source / 'core'

version_source          = 'ReleaseNotes.txt'
version_line_prefix     = "BUILD_"


def write_version_file( payload_path:Path ) -> str:
    with open( str( payload_path / version_source ) ) as file :
        for line in file :
            if line.startswith( version_line_prefix ) :
                version = line.strip( ).split( version_line_prefix )[-1]
                with open( str( payload_path / '__version__.py' ), 'w' ) as version_file :
                    version_string = "__version__ = '" + version + "'"
                    print( version_string, file=version_file, flush=True )
                break
        else:
            raise RuntimeError("Didn't find version line in version source file.", file)
    return version

#----------------------------------------------------------------------#
