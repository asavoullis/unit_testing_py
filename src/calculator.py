
def add(x, y):
    """ Add function"""
    return x + y

def subtract(x, y):
    """ Subtract function """
    return x - y

def multiply(x, y):
    """ Multiply function """
    return x * y

def divide(x, y):
    """ Divide function """
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def power(x, y):
    """ Power function """
    return x ** y

def square_root(x):
    """ Square root function """
    if x < 0:
        raise ValueError('Cannot calculate square root of a negative number!')
    return x ** 0.5

def absolute_value(x):
    """ Absolute value function or modulus """
    return abs(x)

def floor_division(x, y):
    """ Floor Division function """
    if y == 0:
        raise ValueError('Cannot perform floor division by zero!')
    return x // y

def remainder(x, y):
    """ Remainder function or modulo """
    if y == 0:
        raise ValueError('Cannot calculate remainder with zero!')
    return x % y


if __name__ == "__main__":
    # Example usage
    result_add = add(5, 3)
    print("Addition:", result_add)

    result_power = power(2, 3)
    print("Power:", result_power)

    result_sqrt = square_root(25)
    print("Square Root:", result_sqrt)
