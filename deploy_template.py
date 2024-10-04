deploy_template = """@ECHO OFF

SET \"PROJECT_DIR={0}\"
SET \"GAME_DIR={3}\"
SET \"PROFILE={4}\"

CD /D %PROJECT_DIR%

TASKKILL /F /IM DayZDiag_x64.exe

TIMEOUT 2

CD /D "{5}"

py deploy.py \"%PROJECT_DIR%\"

CD /D GAME_DIR

REM "CLEANUP LOGS"

DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.rpt"
DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.log"
DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.ADM"
DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.mdmp"



START "" \"{1}\" -server \"-profiles=%PROFILE%\" -filePatching \
"-mod={2}" \
-port=2302 -config=serverDZ.cfg -newErrorsAreWarnings=1

TIMEOUT 2

START "" \"{1}\" "-mod={2}" -filePatching \
-name=%PROFILE% -window -newErrorsAreWarnings=1

{6}

"""