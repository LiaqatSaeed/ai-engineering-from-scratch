# Linear Regression

Linear Regression is used to find a relationship between an **input** and an **output** and then use that relationship to make predictions.

Example:

- Input (`x`) = Years of Experience
- Output (`y`) = Salary

## Main Formula

```text
prediction = weight * input + bias
```

Mathematically:

```text
ŷ = wx + b
```

Where:

- `x` = Input
- `y` = Actual Output
- `ŷ` = Predicted Output
- `w` = Weight / Slope
- `b` = Bias / Intercept

---

## 1. Weight / Slope

Weight tells us the **pace at which output changes when input changes**.

Formula:

```text
weight = output difference / input difference
```

Or:

```text
w = (y2 - y1) / (x2 - x1)
```

Example:

```text
Point 1:
x1 = 3
y1 = 4700

Point 2:
x2 = 7
y2 = 10300
```

Calculate differences:

```text
Input Difference = 7 - 3
                 = 4

Output Difference = 10300 - 4700
                  = 5600
```

Calculate weight:

```text
weight = 5600 / 4
weight = 1400
```

This means the output changes by `1400` for every `1` unit increase in input.

---

## 2. Bias / Intercept

Bias represents the base value of the line.

Formula:

```text
bias = actual_output - (weight * input)
```

Or:

```text
b = y - wx
```

Example:

```text
bias = 4700 - (1400 * 3)

bias = 4700 - 4200

bias = 500
```

So:

```text
bias = 500
```

---

## 3. Prediction

Now we know:

```text
weight = 1400
bias = 500
```

Our model becomes:

```text
prediction = 1400 * input + 500
```

If the new input is:

```text
input = 10
```

Then:

```text
prediction = (1400 * 10) + 500

prediction = 14000 + 500

prediction = 14500
```

Final prediction:

```text
14500
```

---

## Program Flow

```text
Actual Data
    ↓
Calculate Input Difference
    ↓
Calculate Output Difference
    ↓
Calculate Weight / Slope
    ↓
Calculate Bias / Intercept
    ↓
Take New Input
    ↓
Make Prediction
```

The Python program takes the actual data from the user instead of using hard-coded values.

It then calculates:

```text
Weight
Bias
Prediction
```

## Key Formulas

```text
weight = (y2 - y1) / (x2 - x1)

bias = y - (weight * x)

prediction = (weight * input) + bias
```

## Key Takeaway

`Weight` tells us the **pace of change**.

`Bias` tells us the **base/starting value**.

Together they create the Linear Regression model:

```text
prediction = weight * input + bias
```