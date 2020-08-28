
from os import stat
from pwd import getpwuid

import os.path, time




dir = "BSHDEV-master"
arr = os.listdir(dir)

for file in arr:
    filename, file_extension = os.path.splitext(file)
    size = os.path.getsize( dir + "/" + file)
    author = getpwuid(stat(dir + "/" + file).st_uid).pw_name
    modify_date = time.ctime(os.path.getmtime(dir + "/" + file))
    create_date = time.ctime(os.path.getctime(dir + "/" + file))
    access_date = time.ctime(os.path.getatime(dir + "/" + file))


    print(filename, file_extension, str(size) + "-bytes", author, modify_date, create_date, access_date)
