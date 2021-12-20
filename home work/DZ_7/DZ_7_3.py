import shutil
source = "D:\Tutorial\Python\DZ\DZ_7\my_project"
destination = "D:\Tutorial\Python\DZ\DZ_7\zakavyrka"  #### \templates-но если делать как в методичьке выдает ошибку на \t
new_dir = shutil.move(source, destination)
print (new_dir)
