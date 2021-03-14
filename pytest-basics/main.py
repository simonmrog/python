def sum_numbers(x, y):
    return x + y


def write_file(fpath, data):
    with open(fpath, 'w') as file:
        file.write(data)


class calculator:
    # Test sum and not sum_numbers and nested functions
    def sum(self, x, y):
        return sum_numbers(x, y)
