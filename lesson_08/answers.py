# Найти все файлы в каталоге занятий, включая подкаталоги.
# Вывести список файлов в порядке уменьшения их размера в виде:
#   dir3/file1 123456
#   dir2/somedir/file2 93423  ...
#   fileN 14
# Путь до файла и размер должны быть аккуратно размещены в соответствующих колонках.

import os

all_files = {}
max_len = 0
max_size = 0
for dirpath, dirs, files in os.walk('..'):
    for file in files:
        path = os.path.join(dirpath, file)
        stat = os.stat(path)
        size = stat.st_size
        all_files[path] = size
        max_len = max(max_len, len(path))
        max_size = max(max_size, size)

format_string="{{:{}}}\t{{:{}d}}".format(max_len, len(str(max_size)))
for file, size in sorted(all_files.items(), key=lambda x: x[1], reverse=True):
    print(format_string.format(file, size))


# Найти все дубликаты файлов в подкаталоге. Дубликат определять по одинаковому
# содержимому файла. Результат вывести в виде:
# 12345 байт
#    /path1/file1
#    /path2/subpath2/another-file
# 4321 байт
#    ...

print("="*100)

import os
import hashlib
from collections import defaultdict

file_hashes = defaultdict(list)
for dirpath, dirs, files in os.walk('..'):
    for file in files:
        path = os.path.join(dirpath, file)
        with open(path, 'rb') as f:
            key = hashlib.md5(f.read()).hexdigest()
            file_hashes[key].append(path)

for hash, paths in file_hashes.items():
    if len(paths) > 1:
        size = os.stat(paths[0]).st_size
        print(size)
        for path in paths:
            print("\t{}".format(path))


# Просканировать все файлы занятий и найти все импортируемые модули.
# Вывести для каждого модуля в скольких файлах он был импортирован.
#  - os: 3
#  - pickle: 1
#  - defaultdict: 5

print("="*100)

import re

imports = defaultdict(set)
for dirpath, dirs, files in os.walk('..'):
    for file in files:
        path = os.path.join(dirpath, file)
        if path.endswith('.py'):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            for so in re.finditer('^\s*import\s+(.*?)\s*$', content, re.MULTILINE):
                for module in so.group(1).split(','):
                    imports[module].add(path)
            for so in re.finditer('^\s*from\s+(.*?)\s+import.*$', content, re.MULTILINE):
                for module in so.group(1).split(','):
                    imports[module].add(path)

for module, paths in sorted(imports.items(), key=lambda x: len(x[1]), reverse=True):
    print(module)
    for path in paths:
        print("\t{}".format(path))
