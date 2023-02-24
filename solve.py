
from termcolor import colored
import random
import time
import argparse
import numpy as np
import os


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


def print_rainbow(string, animated=False, delay=0):
    # Define a list of colors
    colors = [
        'red',
        'yellow',
        'green',
        'cyan',
        'blue',
        'magenta'
    ]

    # Split the string into lines
    lines = string.split('\n')

    # Determine the maximum width of each column
    col_widths = [max(len(line.split()[i]) for line in lines)
                  for i in range(len(lines[0].split()))]

    # Print each line with aligned columns and rainbow colors
    for i, line in enumerate(lines):
        words = line.split()
        for j, word in enumerate(words):
            color = colors[j % len(colors)]
            word = word.ljust(col_widths[j])
            print(colored(word, color), end=' ')
        print(colored('', 'white'))
        if animated:
            time.sleep(delay)


def format_variables(values):
    variable_names = [f'x{i+1}: {val:.8f}' for i, val in enumerate(values)]
    return ', '.join(variable_names)


def augment_matrix(a, b):
    # Determine the maximum width of each column
    max_widths = [max([len(str(row[i])) for row in a] + [len(str(b[i]))])
                  for i in range(len(a[0]))]

    # Combine a and b into a single matrix
    ab = [ai + [bi] for ai, bi in zip(a, b)]

    # Convert the matrix to a string
    matrix_string = ''
    for row in ab:
        row_string = ''
        for i in range(len(row)):
            # Add padding to align the columns
            column_width = max_widths[i]
            cell_value = str(row[i]).rjust(column_width)
            # Add rainbow color to each cell value
            color = random.choice(
                ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'])
            cell_value = colored(cell_value, color)
            row_string += cell_value + '  '
        matrix_string += row_string.strip() + '\n'

    # Animate the output line by line and letter by letter
    for line in matrix_string.split('\n'):
        for letter in line:
            print(letter, end='', flush=True)
            time.sleep(0.01)  # pause for 0.01 seconds between each letter
        print()
        time.sleep(0.1)  # pause for 0.1 seconds between each line


if __name__ == '__main__':
    os.system('pip install -r requirements.txt')  # install requirements
    os.system('cls' if os.name == 'nt' else 'clear')  # clear screen

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, help='input matrix A')
    parser.add_argument('-b', type=str, help='input vector b')
    args = parser.parse_args()

    A = np.array(eval(args.a))
    b = np.array(eval(args.b))

    example = 'python solve.py -a "[[1, 3, 7, 2], [3, 4, 1, 2], [4, 9, 1, 2], [1, 3, 7, 5]]" -b "[3, 1, 9, 7]"'

    try:
        x = gauss(A, b)
        x = format_variables(x)
        # make the color of the rainbow
        augment_matrix(A, b)

    except:
        x = f'Error: Invalid input. Example: {example}'
    finally:

        print_rainbow(str(x), animated=True, delay=0.1)
