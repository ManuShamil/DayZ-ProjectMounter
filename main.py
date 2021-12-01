import sys
import glob
from colorama import Fore, Back, Style, init
import json
import os
import tempfile
import pathlib

from symlink import SimLink
from dependency import Dependency
from projectfile import ProjectFile

from deploy_template import deploy_template

class Main:

    project_settings = None

    def __init__( self ):

        if len( sys.argv ) < 5:
            print("EXITING PROJECT MOUNT : NOT ENOUGH PARAMETERS ")

        # for colorama
        init( convert=True )
            
        self.project_dir = sys.argv[1]
        self.project_name = sys.argv[2]
        self.project_settings_file = self.project_dir + "\\" + sys.argv[3]
        self.work_drive = sys.argv[4]

        self.project_settings = json.loads( open( self.project_settings_file ).read() )

        # resolve settings
        self.project_settings["dependencies"] = [ self.resolve_settings(x) for x in self.project_settings["dependencies"]]

        # for global access
        self.project_settings["project_dir"] = self.project_dir
        self.project_settings["project_name"] = self.project_name
        self.project_settings["work_drive"] = self.work_drive


        print( self.project_settings)

        print(f"========================================================\n\
MOUNTING PROJECT\n\
========================================================\n\
{ Fore.RED }{Back.WHITE}PROJECT_DIR => {self.project_dir} \n\
PROJECT_NAME => { self.project_name } \n\
PROJECT_SETTINGS => { self.project_settings_file}{ Style.RESET_ALL }")

        self.cleanup_previous_project()

        self.mount_projects()
        self.mount_dependencies()

        self.create_dayzprojectfile()
        self.create_deploy_batch()
        self.create_gitignore()
        self.link_project_files()

    def cleanup_previous_project( self ):

        print("====================     CLEANING UP PREVIOUS PROJECT    =========================")

        sim_links = SimLink.get_symlinks( self.work_drive )

        if len( sim_links ) <= 0:
            print("NOTHING TO CLEANUP")

            return

        cleaned_count = 0
        for x in sim_links:
            if SimLink.unlink( x ) == True:
                cleaned_count += 1

        print(f"CLEANUP UP {cleaned_count} MOD(s) FROM WORKDRIVE")

    def mount_projects( self ):

        print("=====================    MOUNTING PROJECTS   ================================== ")

        # get number of subdirs in the project directory (each dir => single pbo)
        project_folders = glob.glob( "{0}/*/".format( self.project_dir ) )

        linked_count = 0

        # simlink each folder
        for folder in project_folders:
            self.mount_project( folder )
            linked_count += 1

        print(f"MOUNTED { linked_count } FOLDER(s) ONTO WORKDRIVE")

        print("================================================================================ ")

    def mount_dependencies( self ):

        print("=====================    MOUNTING DEPENDENCIES   =============================== ")

        dependency = Dependency( self.project_settings["dependencies"] )
        dependency.mount(  self.work_drive )

        linked_count = 1

        print(f"MOUNTED { linked_count } FOLDER(s) ONTO WORKDRIVE")

        print("================================================================================ ")



    def mount_project( self, folder ):

        #print( "===> MOUNTING \n  => {0}".format( folder ) )


        SimLink.link( folder , self.work_drive)

    def create_dayzprojectfile( self ):

        projectfile = ProjectFile( self.project_settings )


    def resolve_settings( self, setting ):

        
        type = setting["type"]

        if type == "setting":

            path = setting["path"]

            config_path = f"{self.project_dir}\\{path}.json"

            if( os.path.exists( config_path )):
                config = json.loads( open( config_path).read() )

                return config

            if ( os.path.exists( path )):
                config = json.loads( open( path ).read() )

                return config
            

        return setting

    def create_deploy_batch( self ):

        print( f"=====================    CREATING DEPLOY SCRIPT  ================================== ")

        dependency_mods = set()

        if "dependencies" in self.project_settings:

            for x in self.project_settings["dependencies"]:

                path = x['path']
                path_array = path.replace('/','\\').split('\\')

                mod_location = ""

                for folder in path_array:
                    if folder.lower() == "addons":
                        break

                    mod_location += folder + '\\'

                mod_location.rstrip('\\')

                dependency_mods.add( mod_location)

        
        temp_folder = f"{tempfile.gettempdir()}\\DayZProjectMounter"
        deploy_folder = f"{temp_folder}\\Deploy"

        mod_string = ""

        for x in dependency_mods:
            mod_string += x.rstrip('\\') + ";"

        mod_string += deploy_folder

        dayz_path = self.project_settings["game_dir"] + "/" + "DayZDiag_x64.exe"

        cur_dir = pathlib.Path(__file__).parent.absolute()


        deploy_cmd = deploy_template.format( self.project_dir, dayz_path, mod_string, self.project_settings["game_dir"], self.project_settings["profile"], cur_dir, self.project_settings["work_drive"] )

        f = open("deploy.bat", "w")
        f.write( deploy_cmd )

        print( f"=====================    CREATED DEPLOY SCRIPT   ================================== ")

    def create_gitignore( self ):

        if not os.path.exists( '.gitignore'):
            f = open('.gitignore', 'w')
            f.write('deploy.bat\ndayz.gproj')
        else:
            ignore = open('.gitignore').read().split('\n')
            ignore = [ x for x in ignore if x != '']

            print( ignore )

            if 'dayz.gproj' not in ignore:
                ignore.append( 'dayz.gproj' )
            
            if 'deploy.bat' not in ignore:
                ignore.append('deploy.bat')

            txt = ""
            
            i = 0
            for x in ignore:

                txt += x

                if i < len(ignore) - 1:
                    txt += '\n'

                i +=1 

            f = open('.gitignore', 'w')
            f.write(txt)          

    def link_project_files( self ):

        files = [ 'dayz.gproj', 'deploy.bat'] 

        for x in files:

            SimLink.link_file( f"{self.project_dir}/{x}", self.work_drive )     


        
                    
    





if __name__ == "__main__":
    main = Main()