import os
import shutil
########################CAUTION!!!!!############################################################################
################PERMANENTLY DELETES! DOES NOT GO TO RECYCLEBIN##################################################



# os.unlink(path)   #deletes file with path
# os.rmdir(path)    #deletes empty folder with path


# shutil.rmtree(os.path.join(os.getcwd(), 'testFolder2')) #deletes folder with all files in it


################################################################################################################
################################################################################################################

#send2trash comes with the pip script
#it sends the file/folder to the recyclebin, instead of deleting permanently

import send2trash

send2trash.send2trash(os.path.join(os.getcwd(), 'testFolder1'))
