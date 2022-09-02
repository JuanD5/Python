from functions import divide


def test_divide():
    dividend = 15
    divisor = 3 
    result = 5 
    assert divide(dividend=dividend, divisor=divisor) == result