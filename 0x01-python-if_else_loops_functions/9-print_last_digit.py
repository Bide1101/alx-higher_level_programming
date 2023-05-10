def print_last_digit(number):
    if number < 0:
        number *= -1
    lastN = number % 10
    print("{:d}".format(lastN), end="")
    return lastN
