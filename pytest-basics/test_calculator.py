import pytest
from calculator import sum

test_data = [
    (2, 3, 5),
    (3, -4, -1),
    (-3, -4, -7),
    (3, 4, 7),
    (4, 3, 7)
]


@pytest.mark.parametrize("x,y,expected", test_data)
def test_sum(x, y, expected):
    assert sum(x, y) == expected
