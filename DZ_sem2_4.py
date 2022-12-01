import random
def write_file(number):
    with open('file.txt', 'w') as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2*number)}\n")
def read_file():
    with open('file.txt', 'r') as data:
        indexs = list(map(int,data.readlines()))
    return indexs