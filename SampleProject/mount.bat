SET "MOUNTER_PATH=C:\Users\manu_\Documents\GitHub\DayZ-ProjectMounter\main.py"


SET MYPATH=%cd%

SET "PROJECT_FOLDER=%MYPATH%"
SET "PROJECT_NAME=SampleProject"
SET "PROJECT_SETTINGS=project.json"
SET "WORK_DRIVE=P:"


py %MOUNTER_PATH% %PROJECT_FOLDER% %PROJECT_NAME% %PROJECT_SETTINGS% %WORK_DRIVE%