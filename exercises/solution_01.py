####
# Exercise 1
# Starting with the basics of numpy
import re
import sys
import numpy as np


def print_versions():
    python = re.search(r'^[\d+\.]+',sys.version).group()
    numpy = np.__version__
    return print('Python Version:\t{}\nNumpy Version:\t{}'.format(python, numpy))


def create_1d_tensor(lst):
    total_len = np.prod(np.shape(lst))
    if total_len == 0:
        tensor = np.arange(9)
    else:
        tensor = np.array(lst).reshape(int(total_len),)
    return tensor
# create_1d_tensor(np.arange(9).reshape(3,3))


def test_0(ary):
    test = np.all(np.array(ary))
    if test:
        print('False')
    elif not test:
        print('True')
    else:
        print('Invalid')
    return
# print(test_0(np.arange(5)))
# print(test_0([3,4,5]))  


def test_all_0(lst):
    test = np.any(np.array(lst))
    if test:
        print('False')
    elif not test:
        print('True')
    else:
        print('Invalid')
    return
print(test_all_0([0,0,1]))

def main():
    """ Returns version info """
    print_versions()
    array_1 = np.add(np.arange(9),1).reshape(3,3)
    print('Test array:\n{}\nConvert to 1-D array\n{}\n'\
        'Test if contains 0:\t{}\n'\
        'Test if all 0s:\t{}'.format(array_1, create_1d_tensor(array_1),
        test_0(array_1),test_all_0(array_1)))
    # print(create_1d_tensor(array_1))
    # test_0(array_1)
    # array_2 = np.array([0,0,0])
    # print(np.any(array_2))

if __name__ == "__main__":
    main()

