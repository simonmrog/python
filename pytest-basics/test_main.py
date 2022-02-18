import pytest
from main import sum_numbers, write_file


def test_sum_numbers():
    assert sum_numbers(2, 2) == 4


@pytest.mark.parametrize(
    "input_a,input_b,expected",
    [(3, 2, 5), (2, 3, 5), (sum_numbers(3, 2), 5, 10), (3, sum_numbers(2, 5), 10)],
)
def test_sum_numbers_multi(input_a, input_b, expected):
    assert sum_numbers(input_a, input_b) == expected


def test_tmp_dir(tmpdir):
    data_in = "Hello World"
    fpath = f"{tmpdir}/test.txt"
    write_file(fpath, data_in)

    with open(fpath) as file:
        data_out = file.read()

    assert data_in == "data_out"
