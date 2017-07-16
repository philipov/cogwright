# CogWright
 
--------------------------------------------------------------------------

Make python platform wheels out of an archive containing non-python data. 

Intended for creating platform-specific packaging of pythonic wrappers around prebuilt binary libraries.

Implements the `cog` command. `cog make` will run the standard build procedure in the current working directory. 

Working directory should be the project root of your git repository. 

Module-specific parameters and methods are specified via the `__blueprint__.py` file, which should be in the working directory. 

FTP login credentials may be specified in the `__auth__.py` file, which should be in the working directory, and listed in the `.gitignore` file.

`cog -A download\archivename.zip make` will specify a different archive to use as the module payload.


--------------------------------------------------------------------------
