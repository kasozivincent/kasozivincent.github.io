from typing import TypeVar

T = TypeVar('T')

# Custom refinement type decorator


def refine_type(predicate):
    def decorator(cls):
        class RefinedType(cls):
            def __init__(self, value):
                if not predicate(value):
                    raise ValueError(
                        "Value does not satisfy the refinement type predicate.")
                super().__init__(value)

        return RefinedType

    return decorator

# Example refinement type predicate


def positive_integer(value):
    return isinstance(value, int) and value > 0

# Usage


@refine_type(positive_integer)
class PositiveInteger:
    def __init__(self, value: int):
        self.value = value


# Creating instances
x = PositiveInteger(5)  # Valid, satisfies the refinement type predicate
# Raises ValueError, does not satisfy the refinement type predicate
y = PositiveInteger(-2)
