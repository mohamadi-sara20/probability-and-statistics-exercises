import numpy as np


def calculate_b(X, y):
    A = np.dot(X.T, X)
    g = np.dot(X.T, y).reshape(X.shape[1], 1)
    return np.dot(np.linalg.inv(A), g)


if __name__ == "__main__":
    y = [6.40, 15.05, 18.75, 30.25, 44.85, 48.94, 51.55, 61.50, 100.44, 111.42]
    x0 = [1 for i in range(10)]
    x1 = [1.32, 2.69, 3.56, 4.41, 5.35, 6.20, 7.12, 8.87, 9.80, 10.65]
    x2 = [1.15, 3.40, 4.10, 8.75, 14.82, 15.15, 15.32, 18.18, 35.19, 40.40]
    X = np.stack((x0, x1, x2), axis=1)
    b = calculate_b(X=X, y=y)
    print(f"The model: {b[0][0]:.4f} + {b[1][0]:.4f}x1 + {b[2][0]:.4f}x2")
    