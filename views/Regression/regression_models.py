import numpy as np
from sklearn.metrics import r2_score

def linear_regression(x, y):
    if len(x) < 2:
        return None, None, None
    m, c = np.polyfit(x, y, 1)
    y_pred = m * np.array(x) + c
    r2 = r2_score(y, y_pred)
    return lambda x_val: m * x_val + c, f"y = {m:.2f}x + {c:.2f}", r2

def polynomial_regression(x, y, degree=2):
    if len(x) <= degree:
        return None, None, None
    coeffs = np.polyfit(x, y, degree)
    poly_func = np.poly1d(coeffs)
    y_pred = poly_func(x)
    r2 = r2_score(y, y_pred)
    equation = "y = " + " + ".join([f"{coeff:.2f}x^{i}" for i, coeff in enumerate(coeffs[::-1])])
    return poly_func, equation, r2
