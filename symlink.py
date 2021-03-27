import os
import re
import glob

class SimLink:
    def get_symlinks( dir ):
        """
            returns full path of symlinks in given directory
        """

        # get folders in directory
        files_in_dir = glob.glob( "{0}/*/".format( dir ) )

        # filter out symlinks
        sym_links = [ x for x in files_in_dir if os.path.islink( x ) ]
        sym_links = [ x.replace("/","\\") for x in sym_links]

        return sym_links


    def unlink( dir ):

        # deletes symlink

        if ( os.path.exists( dir )) :
            print("UNLINKING => {0}".format( dir ) )

            res = os.popen( "rmdir {0}".format( dir )).read()

            if res != "":
                print("=> FAILED")
            else:
                print("=> SUCCESS")

            return True

        return False

    def link( folder, workdrive):

        # creates a symlink

        folder = folder.replace("/","\\")

        path_array = folder.split( '\\')

        folder_name = path_array[ len(path_array) - 2]

        workdrive_path = f"{workdrive}\\{folder_name}"

        print( "=> {0} => {1}".format( workdrive_path, folder ) )

        res = os.symlink( folder, workdrive_path)
