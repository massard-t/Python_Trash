#!/usr/bin/python3.5
import numpy as np
import sys
from io import StringIO


def txt_to_matrix(ftxt):
    with open(ftxt, 'r') as f:
        ftxt = f.read()
    ftxt = ftxt.replace(' ', '0')
    ftxt = ftxt.replace('+', '1')
    ftxt = ftxt.replace('@', '2')
    ftxt = ftxt.replace('#', '3')
    print(ftxt)
    txt = StringIO(ftxt)
    matrix = np.loadtxt(txt, delimiter='\n')
    # print(matrix)
    return (matrix)

if __name__ == '__main__':
    txt_to_matrix(sys.argv[1])
