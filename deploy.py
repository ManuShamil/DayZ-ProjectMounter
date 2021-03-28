import sys
import glob
import os
import shutil
import subprocess

import tempfile

class Main:
    
    project_dir = ""
    temp_folder = ""
    deploy_folder = ""

    def __init__( self ):

        if len( sys.argv ) < 2:

            print("NOT ENOUGH PARAMETERS")

            return

        self.project_dir = sys.argv[1]

        self.temp_folder = f"{tempfile.gettempdir()}\\DayZProjectMounter"
        self.deploy_folder = f"{self.temp_folder}\\Deploy\\Addons"

        self.clear_deploy_folder()

        self.pack_pbos()

    def clear_deploy_folder( self ):

        shutil.rmtree( self.deploy_folder )

        os.mkdir( self.deploy_folder )

    def pack_pbos( self ):

        folders = self.get_project_foldernames()

        for x in folders:

            subprocess.call(["MakePbo.exe", '-PsW', '-X=thumbs.db,*.h,*.dep,*.cpp,*.bak,*.png,*.log,*.pew, *.hpp,source,*.tga,*.bat', f"P:/{ x }", "/".join([ self.deploy_folder, x + '.pbo'])])



    def get_project_foldernames( self ):

        project_folders = glob.glob( f"{self.project_dir}/*/" )

        folder_names = [ self.get_folder_name(x) for x in project_folders ]

        return folder_names


    def get_folder_name( self, folder_path):

        folder_path = folder_path.replace('\\','/')
        folder_path_array = folder_path.split('/')

        folder_name = folder_path_array[ len( folder_path_array) - 2]

        return folder_name

if __name__ == "__main__":
    
    main = Main()