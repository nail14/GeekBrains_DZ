###Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates

import shutil
source = "D:\Tutorial\Python\DZ\DZ_7\my_project"

destination = r"D:\Tutorial\Python\DZ\DZ_7\templates"  ####  \t  r разобрался

new_dir = shutil.move(source, destination)
print (new_dir)
