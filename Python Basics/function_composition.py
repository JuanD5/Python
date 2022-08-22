import functools
from typing import Callable

ComposableFunction = Callable[[float],float]


def compose(*functions: ComposableFunction) -> ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)


def addthree(x: float) -> float:
    return x + 3


def multiplybytwo(x: float) -> float:
    return x * 2


def main():
    x = 12
    x = addthree(x)
    x = addthree(x)
    x = multiplybytwo(x)
    x = multiplybytwo(x)
    print(f"result : {x}")


# With function composition
# not that readble 
def main_2():
    x = 8
    result = multiplybytwo(multiplybytwo(addthree(addthree(x))))
    print(f"result : {result}")


if __name__ == "__main__":
    main_2()
