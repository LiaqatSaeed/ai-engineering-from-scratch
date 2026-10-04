# Loss Function - Mean Squared Error (MSE)

# Model predictions
predictions = [1400, 2500, 3500]

# Actual values
actual_values = [1500, 2700, 3200]

total_squared_error = 0

# Calculate error for every data point
for i in range(len(predictions)):

    prediction = predictions[i]
    actual = actual_values[i]

    # Error
    error = prediction - actual

    # Squared Error
    squared_error = error ** 2

    # Add to total
    total_squared_error += squared_error

    print("Data Point:", i + 1)
    print("Prediction:", prediction)
    print("Actual:", actual)
    print("Error:", error)
    print("Squared Error:", squared_error)
    print()


# Calculate MSE
number_of_data_points = len(predictions)

mse = total_squared_error / number_of_data_points


print("----- Final Result -----")

print("Total Squared Error:", total_squared_error)
print("Number of Data Points:", number_of_data_points)
print("MSE:", mse)