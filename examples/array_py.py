import cython

def test():
    p: cython.int[1000] = [0] * 1000

    p[0] = 100
