###Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates

import shutil
source = "D:\Tutorial\Python\DZ\DZ_7\my_project"
destination = "D:\Tutorial\Python\DZ\DZ_7\zakavyrka"  #### \templates-но если делать как в методичьке выдает ошибку на \t
new_dir = shutil.move(source, destination)
print (new_dir)
