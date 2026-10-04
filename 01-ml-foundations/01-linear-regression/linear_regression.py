# Linear Regression from Scratch

print("=== Linear Regression ===")

# Get two actual data points from the user
x1 = float(input("Enter first input (x1): "))
y1 = float(input("Enter first actual output (y1): "))

x2 = float(input("Enter second input (x2): "))
y2 = float(input("Enter second actual output (y2): "))

# Calculate differences
input_difference = x2 - x1
output_difference = y2 - y1

# Calculate weight / slope
weight = output_difference / input_difference

# Calculate bias / intercept
bias = y1 - (weight * x1)

# Show calculations
print("\n--- Model Parameters ---")
print("Input Difference:", input_difference)
print("Output Difference:", output_difference)
print("Weight / Slope:", weight)
print("Bias / Intercept:", bias)

# Get new input for prediction
new_input = float(input("\nEnter input for prediction: "))

# Make prediction
prediction = (weight * new_input) + bias

print("\n--- Prediction ---")
print("Input:", new_input)
print("Prediction:", prediction)