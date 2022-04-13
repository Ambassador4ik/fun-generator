import dictsaver


def collect(lines):
    dict = dictsaver.read()
    for i in range(len(lines)):
        flag = 1
        for j in range(len(dict)):
            if lines[i] == dict[j][0]:
                flag = 0
                dict[j][1] = str(int(dict[j][1]) + 1)
        if flag:
            dict.append([lines[i], '1'])

    dictsaver.write(dict)
