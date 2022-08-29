from dataclasses import dataclass
from enum import Enum


class OrgRole(Enum):
    CEO = "ceo"
    PRESIDENT = "president"
    STAFF = "staff"


@dataclass
class Employee:
    name: str
    role: OrgRole


def main() -> None:
    louis = Employee(name="Louis", role=OrgRole.STAFF)
    print(louis)
    sarah = Employee(name="Sarah", role=OrgRole.CEO)
    print(sarah)
    print(type(sarah.role), sarah.role)
    print(type(sarah.role.value), sarah.role.value)


if __name__ == "__main__":
    main()
