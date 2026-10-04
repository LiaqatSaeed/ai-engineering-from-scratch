# Derivatives from Scratch
# Goal:
# Calculate:
#   1. Loss for every data point
#   2. dLoss/dw for every data point
#   3. MSE
#   4. dMSE/dw

inputs = [1, 2, 3]
actual_values = [1500, 2500, 3500]

weight = 800
bias = 500

total_loss = 0
total_derivative = 0

for i in range(len(inputs)):

    x = inputs[i]
    actual = actual_values[i]

    # Step 1: Prediction
    prediction = (weight * x) + bias

    # Step 2: Error
    error = prediction - actual

    # Step 3: Loss
    loss = error ** 2

    # Step 4: Derivative of Loss with respect to Weight
    # dLoss/dw = 2 * Error * Input
    derivative = 2 * error * x

    total_loss += loss
    total_derivative += derivative

    print("Data Point:", i + 1)
    print("Input:", x)
    print("Actual:", actual)
    print("Prediction:", prediction)
    print("Error:", error)
    print("Loss:", loss)
    print("dLoss/dw:", derivative)
    print()


number_of_data_points = len(inputs)

# Mean Loss
mse = total_loss / number_of_data_points

# Mean Derivative
mean_derivative = total_derivative / number_of_data_points


print("----- Final Result -----")
print("Weight:", weight)
print("Total Loss:", total_loss)
print("MSE:", mse)
print("Total Derivative:", total_derivative)
print("dMSE/dw:", mean_derivative)