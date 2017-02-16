# import shutil
#
# f1 = open('app.py', 'r')  # русский комментарий
# f2 = open('app2.py', 'w')
#
# print(f1.tell())
# f1.seek(3)
# print(f1.read(30))
# print(f1.tell())
# print(f1.readline())
# print(f1.tell())
#
# import os
#
# for dirname, dirs, files in os.walk('..'):
#     print(dirname, dirs, files)
#
# os.remove('app2.py')
# shutil.rmtree('test')

import re
m = re.search('.rm(tr)ee', "shutil.rmtree('test')")
print(m.group(1))


