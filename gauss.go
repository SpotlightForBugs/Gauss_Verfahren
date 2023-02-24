package main

import "fmt"

func main() {
    A := [][]float64{{1, 3, 7}, {3, 4, 1}, {4, 9, 1}}
    b := []float64{3, 1, 9}
    x := gauss(A, b)
    fmt.Println(x)
}

func gauss(A [][]float64, b []float64) []float64 {
    n := len(A)

    // Vorwärtselimination
    for k := 0; k < n-1; k++ {
        for i := k + 1; i < n; i++ {
            factor := A[i][k] / A[k][k]
            for j := k + 1; j < n; j++ {
                A[i][j] -= factor * A[k][j]
            }
            b[i] -= factor * b[k]
        }
    }

    // Rückwärtssubstitution
    x := make([]float64, n)
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i := n - 2; i >= 0; i-- {
        s := b[i]
        for j := i + 1; j < n; j++ {
            s -= A[i][j] * x[j]
        }
        x[i] = s / A[i][i]
    }

    return x
}
