# Gradient Descent from Scratch

inputs = [1, 2, 3]
actual_values = [1500, 2500, 3500]

weight = 800
bias = 500

# Hyperparameter chosen by us
learning_rate = 0.01

# Number of times we process the full dataset
epochs = 10


for epoch in range(epochs):

    total_loss = 0
    total_derivative = 0

    # Process every data point
    for i in range(len(inputs)):

        x = inputs[i]
        actual = actual_values[i]

        # 1. Prediction
        prediction = (weight * x) + bias

        # 2. Error
        error = prediction - actual

        # 3. Loss
        loss = error ** 2

        # 4. Derivative for this data point
        derivative = 2 * error * x

        total_loss += loss
        total_derivative += derivative

    number_of_data_points = len(inputs)

    # 5. Mean Loss
    mse = total_loss / number_of_data_points

    # 6. Mean Derivative = Gradient
    gradient = total_derivative / number_of_data_points

    print("Epoch:", epoch + 1)
    print("Weight before update:", weight)
    print("MSE:", mse)
    print("Gradient:", gradient)

    # 7. Gradient Descent
    step = learning_rate * gradient

    # 8. Update Weight
    weight = weight - step

    print("Step:", step)
    print("Weight after update:", weight)
    print("--------------------")