#!/usr/bin/python3

import re
import sys


def get_first_anchor(path):
    f = open(path)
    while(1):
        l = f.readline()
        if not l:
            break
        elif re.match("#+ ", l):
            f.close()
            return '#' + (l[l.find(' ')+1:-1]).lower().replace(' ', '-')
    f.close()
    return '#'


def uni_file(path, n=0):
    f = open(path)
    content = f.readlines()
    new_content = []
    for i in content:
        if (n != 0) and re.match("#+ ", i):
            new_content.append(n*'#'+i)
        elif re.match(" \* \[.+\]\(.+\.md\)", i):
            ref_path = re.search("\(.+\.md\)", i).group()
            ref_path = ref_path[1:-1]
            new_content += ['\n']
            new_content += uni_file(ref_path, n+1)
        elif re.search("\[.+\]\(.+\.md\)", i):
            ref = re.search("\[.+\]\(.+\.md\)", i)
            start = ref.start()
            end = ref.end()
            ref_path = ref.group()
            ref_path = ref_path[ref_path.find('(')+1:-1]
            if path.rfind('/') != -1:
                ref_path = path[:path.rfind('/')] + '/' + ref_path
            new_line = i[:i.find('(', start)+1]+get_first_anchor(ref_path)+i[end-1:]
            new_content.append(new_line)
        else:
            new_content.append(i)
    f.close()
    return new_content


def main():
    l0_file = [i for i in sys.argv if i.find('/') == -1]
    new_content = []
    for i in l0_file:
        new_content += uni_file(i)
        new_content += ['\n']
    f = open("uni.md", "w")
    f.writelines(new_content)
    f.close()


if __name__ == '__main__':
    main()
