import os
from PIL import Image
import glob
import shutil


## Type here the respective post name:
post_name = 'p137p'




def createFolder(directory):
    '''
    Creates a folder in the place of the root directory
    
    Args: 
        directory (string): Name that should be given to the created folder
        
    Returns:
        New folder at the current directory
    '''
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)



root_dir = os.getcwd()
root_dir = root_dir.replace('\\', '/')
print(root_dir)
temp_dir = root_dir + '/pics_temp'
print(temp_dir)
backup_dir = root_dir + '/pics_backup'
print(backup_dir)
target_dir = root_dir + '/pics_renamed'
print(target_dir)


createFolder(root_dir + '/pics_temp')
print('Folder 1 created')
createFolder(root_dir + '/pics_backup')
print('Folder 2 created')
createFolder(root_dir + '/pics_renamed')
print('Folder 3 created')



for f in os.listdir(root_dir):
    if f.endswith((".png")):
        shutil.copy(os.path.join(root_dir, f), backup_dir)
        shutil.move(os.path.join(root_dir, f), temp_dir)



for i, filename in enumerate(os.listdir(temp_dir)):
    os.rename(temp_dir + '/' + filename, target_dir + '/' + post_name + str(i) + ".png")






