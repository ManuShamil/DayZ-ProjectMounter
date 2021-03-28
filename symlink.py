import os
import re
import glob
from heapq import merge

class SimLink:
    def get_symlinks( dir ):
        """
            returns full path of symlinks in given directory
        """

        # get folders in directory
        files_in_dir = glob.glob( "{0}/*/".format( dir ) )
        files_in_dir = list( merge( files_in_dir, glob.glob( "{0}/*.*".format( dir ))))


        # filter out symlinks
        sym_links = [ x for x in files_in_dir if os.path.islink(x) == True ]

        sym_links = [ x.replace("/","\\") for x in sym_links]

        print( sym_links)

        return sym_links


    def unlink( dir ):

        # deletes symlink

        if ( os.path.exists( dir )) :
            print("UNLINKING => {0}".format( dir ) )

            print( os.path.isdir( dir))
            print( os.path.isfile( dir) )

            if os.path.isdir( dir ):
                res = os.popen( "RMDIR {0}".format( dir )).read()
            else:
                print( dir )
                res = os.popen( "DEL {0}".format( dir )).read()


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

    def link_file( file, workdrive):

        file = file.replace('/','\\')

        file_name = file.split( '\\')
        file_name = file_name[ len( file_name) - 1]

        workdrive_path = f"{workdrive}/{file_name}"

        print( workdrive_path )

        res = os.symlink( file, workdrive_path)
