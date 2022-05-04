####Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок

import os
import yaml


values = ['settings', 'mainapp', 'adminapp', 'authapp']
keys = 'my_project'
dict = {keys: values}


dir_path = [os.makedirs(os.path.join(keys, i)) for i in values if not os.path.exists(os.path.join(keys, i))]

print(os.path.join(os.path.abspath(os.getcwd())[:0], keys))
path = os.path.join(os.path.abspath(os.getcwd())[:0], keys)
for i in values:
    print(os.path.join(path, i))

with open('config.yaml', 'w') as f:
    yaml.dump(path, f)
    for i in values:
        yaml.dump(os.path.join(path, i), f)
    pass
