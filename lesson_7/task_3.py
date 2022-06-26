'''
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
например, во фреймворке django.
'''

import os
import shutil

os.makedirs(os.path.join('my_project', 'my_templates'), exist_ok=True)
comm_path = os.path.join(os.getcwd(), 'my_project', 'my_templates')
templates_path = []
for root, folders, files in os.walk('my_project'):
    if 'templates' in folders:
        templates_path.append(os.path.join(root, 'templates'))

for path in templates_path:
    for temp_folder in os.listdir(path):
        path1 = os.path.join(path, temp_folder)
        path2 = os.path.join(comm_path, temp_folder)
        shutil.copytree(path1, path2, dirs_exist_ok=True)
    print(templates_path)