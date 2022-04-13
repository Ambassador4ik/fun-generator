import random
from math import *


def gen_seed():
    seed = ''
    for i in range(32):
        seed += str(random.randint(0, 9))
    return seed


def gen_numbers(seed):
    nums = []
    count = 0
    for i in range(32):
        if count > 1001:
            break
        for j in range(32):
            if count > 1001:
                break
            for k in range(32):
                num = str(seed[i]) + str(seed[j]) + str(seed[k])
                num = cos(trunc(int(num)**k))
                n = str(num)
                n = n[3:8]
                if n != '' and (13500 <= int(n.rstrip()) <= 40880):
                    nums.append(int(n))
                if count > 1001:
                    break
    return nums


def rand_numbers():
    nums = []
    for i in range(1001):
        nums.append(random.randint(13500, 40880))
    return nums
