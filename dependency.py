import tempfile
import os
import shutil
import glob
from symlink import SimLink

class Dependency:

    dependecies = []

    def __init__(self, dependencies):

        """
        "dependencies": [
            {
                "comments": "for custom pbos with no pre existing templates",
                "type": "pbo",
                "path": "",
                "project_files": {
                    "core": [
                        "JM/CF/Scripts/1_Core"
                    ],
                    "gameLib": [
                        
                    ],
                    "game": [
                        "JM/CF/Scripts/3_Game"
                    ],
                    "world": [
                        "JM/CF/Scripts/4_World"
                    ],
                    "mission": [
                        "JM/CF/Scripts/5_Mission"
                    ]
                }
            }
        ]
        """

        self.dependecies = dependencies

        self.lookup()

    def lookup(self):

        for x in self.dependecies:
            print("FOUND DEPENDENCY => {0}".format( x["path"] ))

    def mount( self, mount_to ):

        temp_folder = f"{tempfile.gettempdir()}\\DayZProjectMounter"
        extracted_folder = f"{temp_folder}\\Extracted"

        # clear extracted folder if already exists
        if os.path.exists( extracted_folder ):
            shutil.rmtree( extracted_folder )

        # create temp folder
        if os.path.exists( temp_folder ) != True:

            os.mkdir( temp_folder )
        
        # create extracted folder inside
        if os.path.exists( extracted_folder ) != True:

            os.mkdir( extracted_folder )



        for x in self.dependecies:

            type = x["type"]
            path = x["path"]

            print( f"MOUNTING => { path }\nTYPE => { type }" )

            if type == "pbo":
                # do not mount if noLoad is set to true

                if "noLoad" in x :
                    if x["noLoad"] == True:
                        continue

                # mount each pbo
                self.mount_pbo( extracted_folder, x )

        # mount all folders in extracted_folder to Workdrive

        extracted = glob.glob( f"{extracted_folder}/*/")

        for x in extracted:
            SimLink.link( x, mount_to)


        print( extracted )

    def mount_pbo( self, to, dependency ):

        pbo_path = dependency["path"]


        print(f"============> EXTRACTING PBO => {to}\n")

        result = os.popen( f"ExtractPbo.exe -P \"{pbo_path}\" \"{to}\"").read()
        

        print(f"\n")

        pass

