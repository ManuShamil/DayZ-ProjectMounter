deploy_template = """@ECHO OFF

SET \"PROJECT_DIR={0}\"
SET \"GAME_DIR={3}\"
SET \"PROFILE={4}\"

CD /D %PROJECT_DIR%
git add *
git commit -m "update"
git push origin dev-live

TASKKILL /F /IM DayZDiag_x64.exe

TIMEOUT 2

CD /D "C:/Users\manu_/Documents/GitHub/DayZ-ProjectMounter"

py deploy.py \"%PROJECT_DIR%\"

CD /D GAME_DIR

REM "CLEANUP LOGS"

DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.rpt"
DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.log"
DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.ADM"
DEL /s /q /f "%GAME_DIR%\%PROFILE%\*.mdmp"



\"{1}\" -server \"-profiles=%PROFILE%\" \
"-mod={2}" \
-port=2302 -config=serverDZ.cfg


"""