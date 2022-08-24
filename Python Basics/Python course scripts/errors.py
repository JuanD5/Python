
class CustomTypeError(TypeError):
    """ Custom error when a error happens

    Args:
        TypeError (): Python build in type error
    """
    def __init__(self, message: str, code: int):
        super().__init__(f"Error code {code} {message}")
        self.code = code


if __name__ == "__main__":
    err = CustomTypeError(message="Ouch an error happened", code=500)
    print(err.__doc__)
