# with open('class.py', 'rb') as f:
#     print(f.read())

# with open('class.py', 'a+', encoding='utf-8') as f:
#     print(f.tell())
#     f.write('# коммент\n')
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     print(f.read())
#     print(f.tell())
# # коммент

# with open('class.py', 'a+', encoding='utf-8') as f:
#     f.seek(1000)
#     f.write('# ho-ho')
#     f.seek(0)
#     print(f.read())
# # коммент
# #  ho-ho

# import os
# for dirname, dirs, files in os.walk('..'):
#     print(dirname, dirs, files)

# import os
# print(__file__)
# print(os.path.dirname(os.path.abspath(__file__)))
#
# print(__file__.replace('/', '\\'))

import os
# os.mkdir('../tmp')
# with open('../tmp/file', 'w') as f:
#     pass
# os.remove('../tmp/file')
# os.rmdir('../tmp')


# import os
# # os.path.isdir('tmp')
# file = 'tmp/subdirs2/file.txt'
# # print(file, os.path.dirname(file))
# os.mkdir('tmp2/subdirs3')
# # os.makedirs(os.path.dirname(file))
# with open(file, 'w') as f:
#     pass

# import os
# import shutil
# os.removedirs('tmp/subdirs3')
# shutil.rmtree('tmp')

# import os
# os.rename('.', '../lesson-9')

# if os.listdir('.'):
#     print('not empty')
#
# dirname, dirs, files = os.walk('.').__next__()
# if len(dirs) + len(files) == 0:
#     print('is empty')
#
# for entry in os.listdir('.'):
#     print(entry, os.path.isdir(entry))

# import os
# import datetime
# stat = os.stat('class.py')
# print(datetime.datetime.fromtimestamp(stat.st_mtime), stat.st_size)

# import pickle
# # from datetime import datetime
# class C:
#     def m(self, x):
#         return x*10
# #     pass
# # c = C()
# # d = C()
# # obj = [{'key': 3}, 15, datetime(2017, 1, 1), c, d]
# # print(obj[3].m(10), d.m(10))
# # # dump = pickle.dumps(obj)
# def m(y):
#     return y*4
# # c.m = m
# # print(obj[3].m(10), d.m(10))
# # print(pickle.loads(dump)[3].m(10), d.m(10))
# #
# # pickle.dump(obj, open('dump.pickle', 'wb'))
# dump2 = pickle.load(open('dump.pickle', 'rb'))
# print(dump2[3].m(5), dump2)




# import re
# for r in re.finditer('number (\d+?)(\d+?)\\?', 'this is number 345?'):
#     print(r.group(0, 1, 2))

import re
text = 'this is digit 345? this is digit 345?'
for r in re.finditer('number (\d+)', text):
    print(r.group(0, 1))

print(re.sub('(number|digit) (\d+)', '\\1 55', text))
