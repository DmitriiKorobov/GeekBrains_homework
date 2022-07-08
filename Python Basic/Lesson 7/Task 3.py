from pathlib import Path as P
import shutil
import os

dir_link = P.cwd()

for element in os.listdir(dir_link):
    if os.path.isdir(element):
        os.chdir(element)
        for i in os.listdir(str(dir_link) + fr'\{element}'):
            if i[-4:] == 'html':
                shutil.move(str(i), fr'{P.cwd()}\templates')
        os.chdir(dir_link)