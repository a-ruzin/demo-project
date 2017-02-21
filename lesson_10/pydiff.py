# Задача 3
# Написать аналог команды diff -y file1 file2 (построчное сравнение двух файлов).
import itertools


def main():
    with open('../lesson-06/a.txt', 'r', encoding='utf-8') as f1, \
            open('../lesson-06/b.txt', 'r', encoding='utf-8') as f2:
        for line in diff(f1, f2):
            print(line)


def diff(f1, f2):
    buf1 = []
    buf2 = []

    def format_output(text1, text2, sign=" "):
        return "{:40} {} {:40}".format(text1[:40], sign, text2[:40])

    def get_diffs(gen1, gen2):
        while True:
            line1 = next(gen1, None)
            line2 = next(gen2, None)

            if line1 is None and line2 is None:
                break
            elif line1 is None:
                yield format_output("", line2, ">")
            elif line2 is None:
                yield format_output(line1, "", "<")
            else:
                yield format_output(line1, line2, "|")

    while True:
        line = next(f1)
        if line:
            try:
                line = line.strip()
                i2 = buf2.index(line)
                for row in get_diffs(iter(buf1), itertools.islice(buf2, i2)):
                    yield row
                yield format_output(line, line)
                buf1, buf2 = [], buf2[i2+1:]
            except ValueError:
                buf1.append(line)
        else:
            for row in get_diffs(iter(buf1), itertools.chain(iter(buf2), f2)):
                yield row
            break

        line = next(f2)
        if line:
            try:
                line = line.strip()
                i1 = buf1.index(line)
                for row in get_diffs(itertools.islice(buf1, i1), iter(buf2)):
                    yield row
                yield format_output(line, line)
                buf1, buf2 = buf2[i1+1:], []
            except ValueError:
                buf2.append(line)
        else:
            for row in get_diffs(itertools.chain(iter(buf1), f1), iter(buf2)):
                yield row
            break

if __name__ == "__main__":
    main()
