#!/usr/bin/python3

import re
import sys


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
