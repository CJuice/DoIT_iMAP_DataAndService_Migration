# Was going to be used for renaming mxd's by adding a standard text bit that could be removed later. The purpose
#   was to copy the originals, which had save issues and other issues, put in a new location. These were to be used
#   in testing and analysis and manipulation and then were to replace the originals.
# We changed our angle of attack and this was never carried out

import os
import shutil

old_dir_root = r"D:\MXD"
new_dir_root = r"D:\MXD\iMAP_3_copies"
directory_names = None
mxd_paths_dict = {}
for dir, dirnames, files in os.walk(r"D:\MXD"):
    directory_names = dirnames
    break

for name in directory_names:
    newpath = os.path.join(new_dir_root,name)
    if os.path.exists(newpath):
        pass
    else:
        os.mkdir(newpath)

for name in directory_names:
    oldpath = os.path.join(old_dir_root,name)
    for dir, dirnames, files in os.walk(oldpath):
        for file in files:
            if file[-3:] == "mxd":
                new_filename = file
                temp = os.path.join(os.path.join(new_dir_root,name), new_filename)
                mxd_paths_dict[os.path.join(os.path.join(old_dir_root,name), file)] = temp

for key, value in mxd_paths_dict.items():
    shutil.copy(key,value)

