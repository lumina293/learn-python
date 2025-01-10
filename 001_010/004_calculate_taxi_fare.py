def calculate_taxi_fare(x):
    if x <= 1:
        return 10
    if x <= 10:
        return 10 + 8.5 * (x - 1)
    return 10 + 8.5 * 9 + 7.5 * (x - 10)


x = 0.5
fare = calculate_taxi_fare(x)
print("It costs", fare, "to go", x, "km")
