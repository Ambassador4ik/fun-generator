import os


def collect_stats(line):
    try:
        os.mkdir("%username%\\AppData\\Roaming\\.fun\\stats")
        os.mkdir("%username%\\AppData\\Roaming\\.fun\\log")
    except FileExistsError:
        with open("%username%\\AppData\\Roaming\\.fun\\log\\log.txt", 'w') as f:
            f.write("[Warning] Directory %username%\\AppData\\Roaming\\.fun\\ already exists!")


