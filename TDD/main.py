def FizzBuzz(value):
    if (value % 3 == 0) and (value % 5 == 0):
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    return str(value)


def FizzBuzz_test(value, expected):
    retval = FizzBuzz(value)
    assert retval == expected