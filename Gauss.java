public class Gauss {
    public static void main(String[] args) {
        double[][] A = {{1, 3, 7}, {3, 4, 1}, {4, 9, 1}};
        double[] b = {3, 1, 9};
        double[] x = gauss(A, b);
        for (double value : x) {
            System.out.print(value + " ");
        }
    }

    public static double[] gauss(double[][] A, double[] b) {
        int n = A.length;

        // Vorwärtselimination
        for (int k = 0; k < n - 1; k++) {
            for (int i = k + 1; i < n; i++) {
                double factor = A[i][k] / A[k][k];
                for (int j = k + 1; j < n; j++) {
                    A[i][j] -= factor * A[k][j];
                }
                b[i] -= factor * b[k];
            }
        }

        // Rückwärtssubstitution
        double[] x = new double[n];
        x[n - 1] = b[n - 1] / A[n - 1][n - 1];
        for (int i = n - 2; i >= 0; i--) {
            double s = b[i];
            for (int j = i + 1; j < n; j++) {
                s -= A[i][j] * x[j];
            }
            x[i] = s / A[i][i];
        }

        return x;
    }
}
