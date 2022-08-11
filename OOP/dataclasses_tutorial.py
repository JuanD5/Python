import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    name: str
    address: str 
    
    # def __init__(self, name, address) -> None:
    #     self.name = name
    #     self.address =  address
        
    # def __str__(self) -> str:
    #     return f"{self.name},{self.address}"


def main() -> None:
    person = Person(name="John", address="123 Main St")
    print(person)


if __name__ == "__main__":
    main()
