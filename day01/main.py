from typing import List
from pathlib import Path
import os
import numpy as np


def read_file(name):
    base_path = Path(__file__).parent
    file_path = os.path.join(base_path, name)
    my_list = []
    with open(file_path) as f:
        current_elf = []
        for line in f:
            line = line.strip()
            if not line:
                my_list.append(current_elf)
                current_elf = []
            else:
                current_elf.append(int(line))

        if current_elf:
            my_list.append(current_elf)
    return my_list


def algo_1(numbers):
    sums = [sum(n) for n in numbers]
    index = np.argmax(sums)
    return sums[index]


def algo_2(numbers):
    sums = [sum(n) for n in numbers]
    # https://stackoverflow.com/questions/10337533/a-fast-way-to-find-the-largest-n-elements-in-an-numpy-array?lq=1
    values = -np.partition(-np.array(sums), 3)[:3]
    return np.sum(values)


if __name__ == '__main__':
    numbers = read_file('input.txt')
    print(algo_1(numbers))
    print(algo_2(numbers))
