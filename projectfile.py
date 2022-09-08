import glob
import os

from project_template import project_template

class ProjectFile:
    
    project_settings = None

    config = ""

    file_paths = ""
    image_files = ""
    widget_files = ""
    core_files = ""
    gamelib_files = ""
    game_files = ""
    world_files = ""
    mission_files = ""
    workbench_files = ""



    def __init__( self, project_settings ):
        self.project_settings = project_settings
        self.config = project_template

        self.create_project_file()

    def create_project_file( self ):

        self.file_paths = self.get_file_paths()

        self.image_files = self.get_project_modules( "image" )
        self.image_files = self.get_dependency_modules( "image" )

        self.widget_files = self.get_project_modules( "widget" )
        self.widget_files = self.get_dependency_modules( "widget" )

        self.core_files += self.get_project_modules( "core" )
        self.core_files += self.get_dependency_modules( "core" )

        self.gamelib_files += self.get_project_modules( "gameLib")
        self.gamelib_files += self.get_dependency_modules( "gameLib")

        self.game_files += self.get_project_modules("game")
        self.game_files += self.get_dependency_modules("game")

        self.world_files += self.get_project_modules("world")
        self.world_files += self.get_dependency_modules("world")

        self.mission_files += self.get_project_modules( "mission" )
        self.mission_files += self.get_dependency_modules( "mission" )

        self.workbench_files += self.get_project_modules( "workbench")
        self.workbench_files += self.get_dependency_modules( "workbench")


        self.create_file()

    def create_file( self ):

        project_dir = self.project_settings["project_dir"]

        #config = project_template.format( self.file_paths, self.image_files, self.widget_files, self.core_files, self.gamelib_files, self.game_files, self.world_files, self.mission_files, self.workbench_files)
        config = project_template.format( "", self.image_files, self.widget_files, self.core_files, self.gamelib_files, self.game_files, self.world_files, self.mission_files, self.workbench_files)
        f = open( f"{ project_dir}/dayz.gproj", "w")
        f.write( config )

    def get_project_modules( self , type):

        project_files = self.project_settings["project_files"]

        modules = ""
        if type in project_files:
            for x in project_files[ type ]:
                modules += f"\"{x}\"" + "\n\t\t\t\t\t\t"
        

        return modules

    def get_dependency_modules( self, type):

        if "dependencies" not in self.project_settings:
            return ""

        dependency_files = self.project_settings["dependencies"]

        modules = ""
        for mod in dependency_files:

            if "project_files" not in mod:
                continue

            project_files = mod["project_files"]

            if type in project_files:
                for x in project_files[ type ]:
                    modules += f"\"{x}\"" + "\n\t\t\t\t\t\t"
        

        return modules

    def get_file_paths( self ):
        
        workdir = self.project_settings["work_drive"]

        folders = glob.glob( f"{workdir}/*/")

        folders = [ self.get_folder_config(x) for x in folders if os.path.islink(x )]

        folder_config = ""

        for x in folders:
            folder_config += f"{x}" + "\n\t\t\t\t"


        return folder_config
        

    def get_folder_config( self, path):

        path = path.replace('\\', '/')

        folder = path.split('/')
        folder = folder[ len(folder) - 2]

        config = """FileSystemPathClass {{
            \t\tName \"{0}\"
            \t\tDirectory \"{1}\"
        \t\t}}""".format( folder, path)

        return config 


