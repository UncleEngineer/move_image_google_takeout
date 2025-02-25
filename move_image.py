# move photo and video file to one folder

import os
from pprint import pprint
import shutil

backup_path = r'C:\Image\Backup\backup_images'
# copy all folder takeout-20250224T104239Z-002 to 'path'
movepath = r'C:\Image\Backup\allphoto'

allfiles = os.listdir(backup_path)

def movefolder(folder):
    fd = os.path.join(backup_path,folder,'Takeout','Google Photos') 
    
    imgfolder = os.listdir(fd)
    # pprint(d)
    for img in imgfolder:
        if img.split('.')[-1] == 'json':
            pass
        else:
            # print(img)
            newpath = os.path.join(fd,img)
            allphoto = os.listdir(newpath)
            screen = []
            for pt in allphoto:
                if pt.split('.')[-1] == 'json':
                    pass
                else:
                    screen.append(pt)
            # pprint(screen)
            for s in screen:
                currentpath = os.path.join(newpath,s)
                #print(currentpath)
                movetofolder = os.path.join(movepath,s)
                print(movetofolder)
                shutil.move(currentpath,movetofolder)
            
for a in allfiles:
    movefolder(a)