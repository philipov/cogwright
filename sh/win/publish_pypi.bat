@setlocal
@ECHO off

set THIS_PATH=%~dp0
set PROJECT_PATH=%THIS_PATH%..\..
set PIP_CONFIG_FILE=%PROJECT_PATH\..\pip.ini
@pushd %PROJECT_PATH%

rem -- ToDo: macro to obtain __version__
rem twine upload dist\smash-0.0.0.zip --comment "make python platform wheels"
twine upload %PROJECT_PATH%\dist\cogwright-0.0.0-py3-none-any.whl --comment "make python platform wheels"

@popd
@endlocal
