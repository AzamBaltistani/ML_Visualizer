# Mathematics

## 1. Linear Regression

**Goal:** Fit a straight line to the data  
**Equation:**  
$$
y = mx + c
$$
Where:

- $ m $: slope
- $ c $: y-intercept

---

### Given Data Points

| x | y |
|---|---|
| 1 | 2 |
| 2 | 3 |
| 3 | 5 |

---

### Step 1: Calculate the slope $$ m $$

$$
m = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}
$$

- $ n = 3 $  
- $ \sum x = 1 + 2 + 3 = 6 $  
- $ \sum y = 2 + 3 + 5 = 10 $  
- $ \sum xy = 1 \cdot 2 + 2 \cdot 3 + 3 \cdot 5 = 2 + 6 + 15 = 23 $  
- $ \sum x^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14 $

$$
m = \frac{3(23) - (6)(10)}{3(14) - 6^2} = \frac{69 - 60}{42 - 36} = \frac{9}{6} = 1.5
$$

---

### Step 2: Calculate intercept $$ c $$

$$
c = \frac{\sum y - m(\sum x)}{n} = \frac{10 - 1.5 \cdot 6}{3} = \frac{10 - 9}{3} = \frac{1}{3} \approx 0.33
$$

---

### Final Linear Equation

$$
y = 1.5x + 0.33
$$

---

## 2. Polynomial Regression (Degree 2)

**Goal:** Fit a curve (parabola)  
**Equation:**  
$$
y = ax^2 + bx + c
$$

We typically use `numpy.polyfit()` or least squares method.

---

### Example Data

| x | y |
|---|---|
| 1 | 6 |
| 2 | 11 |
| 3 | 18 |

Using Python:

```python
import numpy as np

x = [1, 2, 3]
y = [6, 11, 18]

coeffs = np.polyfit(x, y, 2)
print(coeffs)  # Output: [1. 2. 3.]
```

This gives:

- $$ a = 1 $$  
- $$ b = 2 $$  
- $$ c = 3 $$

---

### Final Polynomial Equation

$$
y = 1x^2 + 2x + 3
$$

---

## R² Score (Coefficient of Determination)

Tells how well the model fits the data.

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

Where:

- $ y_i $: actual values  
- $ \hat{y}_i $: predicted values  
- $ \bar{y} $: mean of actual values  

**Interpretation:**

- $ R^2 = 1 $: perfect fit  
- $ R^2 = 0 $: no explanatory power  
- $ R^2 < 0 $: worse than a horizontal mean line

---

### Summary

| Model               | Equation Form            | Method         |
|--------------------|--------------------------|----------------|
| Linear Regression  | $$ y = mx + c $$         | Least Squares  |
| Polynomial (deg=2) | $$ y = ax^2 + bx + c $$  | polyfit / LS   |
| R² Score           | Fit quality (0 to 1)     | R² Formula     |
