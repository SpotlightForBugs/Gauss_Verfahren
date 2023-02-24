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
    x = [0.0] * n
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        s = b[i]
        for j in range(i+1, n):
            s -= A[i][j] * x[j]
        x[i] = s / A[i][i]

    return x


A = [[1, 3, 7], [3, 4, 1], [4, 9, 1]]
b = [3, 1, 9]
x = gauss(A, b)
print(x)
