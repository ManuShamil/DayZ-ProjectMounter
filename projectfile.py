from project_template import project_template

class ProjectFile:
    
    config = ""

    image_files = ""
    widget_files = ""
    core_files = ""
    gamelib_files = ""
    game_files = ""
    world_files = ""
    mission_files = ""



    def __init__( self, project_settings ):
        self.project_settings = project_settings
        self.config = project_template

        self.create_project_file()

    def create_project_file( self ):

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

        print( self.mission_files )

    def get_project_modules( self , type):

        project_files = self.project_settings["project_files"]

        modules = ""
        if type in project_files:
            for x in project_files[ type ]:
                modules += x + "\n"
        

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
                    modules += x + "\n"
        

        return modules

