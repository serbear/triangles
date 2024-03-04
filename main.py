MSG_INVALID_INPUT = "Invalid input. Please enter integers."
MSG_INVALID_RANGE = "Values are not in the range of permitted values."
NOT_A_TRIANGLE = "NotATriangle"
TYPE_EQUILATERAL = "Equilateral"
TYPE_ISOSCELES = "Isosceles"
TYPE_SCALENE = "Scalene"


def triangle_type(a, b, c):
    # Check valid data type.
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return MSG_INVALID_INPUT

    # Check conditions c1, c2, and c3

    if not (1 <= a <= 200 and 1 <= b <= 200 and 1 <= c <= 200):
        return MSG_INVALID_RANGE

    # Check conditions c4, c5, and c6
    if not (a < b + c and b < a + c and c < a + b):
        return NOT_A_TRIANGLE

    # Determine the type of triangle
    if a == b == c:
        return TYPE_EQUILATERAL
    elif a == b or b == c or a == c:
        return TYPE_ISOSCELES
    else:
        return TYPE_SCALENE
