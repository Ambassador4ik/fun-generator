import os


def write(lines):
    try:
        os.mkdir(".fun\\stats")
    except FileExistsError:
        pass

    with open(".fun\\stats\\words.txt", "w", encoding='utf-8') as f:
        for i in range(len(lines)):
            f.write(lines[i][0] + ' ' + lines[i][1] + '\n')


def read():
    with open(".fun\\stats\\words.txt", encoding='utf-8') as f:
        prelines = f.readlines()
        lines = []
        for i in range(len(prelines)):
            lines.append(prelines[i].split(' '))
            lines[i][1] = lines[i][1].rstrip()
        return lines
