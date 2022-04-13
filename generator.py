import random
import seed as s


def generate(seed):
    line = ""
    j = s.gen_numbers(seed)
    for i in range(1000):
        line += chr(j[i])
    return line.encode('utf-8', 'replace').decode()


def generate_random():
    line = ""
    j = s.rand_numbers()
    for i in range(1000):
        line += chr(j[i])
    return line.encode('utf-8', 'replace').decode()


def shuffle(line):
    st = list(line)
    random.shuffle(st)
    result = ''.join(st)
    return result


def update(line):
    for i in range(25):
        st = line[random.randint(1, len(line) - 1)]
        line = line.replace(st, '', 1)
    for i in range(10):
        st = line[random.randint(1, len(line) - 1)]
        line = line.replace(st, ' ', 1)
    return line
