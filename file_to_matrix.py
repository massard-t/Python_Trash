import numpy


def txt_to_matrix(ftxt):
    ftxt.replace("@", "2")
    ftxt.replace(" ", "0")
    ftxt.replace("+", "1")
    ftxt.replace("#", "3")
    print(ftxt)
