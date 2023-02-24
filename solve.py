import argparse
import numpy as np


def gauss(A, b):
    n = len(A)

    # Vorwärtselimination
    for k in range(n-1):
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Rückwärtssubstitution
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        s = b[i]
        for j in range(i+1, n):
            s -= A[i][j] * x[j]
        x[i] = s / A[i][i]

    return x


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, help='input matrix A')
    parser.add_argument('-b', type=str, help='input vector b')
    args = parser.parse_args()

    A = np.array(eval(args.a))
    b = np.array(eval(args.b))

    example = 'python solve.py -a "[[1, 3, 7, 2], [3, 4, 1, 2], [4, 9, 1, 2], [1, 3, 7, 5]]" -b "[3, 1, 9, 7]"'

    try:
        x = gauss(A, b)
    except:
        x = f'Error: Invalid input. Example: {example}'
    finally:
        print(x)
