import shutil
source = "D:\Tutorial\Python\DZ\DZ_7\my_project"
destination = r"D:\Tutorial\Python\DZ\DZ_7\templates"  ####  \t  r разобрался
new_dir = shutil.move(source, destination)
print (new_dir)
