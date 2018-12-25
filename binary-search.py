import random

def recursive_binary_search (data, target, min, max):

    flag = False

    if min <= max:
        mean = (min + max) // 2

        if target == data[mean]:
            flag = True
        elif target < data[mean]:
            flag = recursive_binary_search (data, target, min, mean - 1)
        else:
            flag = recursive_binary_search (data, target, mean + 1, max)

    return (flag)


def iterative_binary_search (data, target, min, max):

    flag = False

    while min <= max:

        mean = (min + max) // 2

        if target == data[mean]:
            flag = True
            min = max + 1
        elif target < data[mean]:
            max = mean - 1
        else:
            min = mean + 1

    return (flag)


def create_list (size):

    list = []
    for i in range (0, size):
        list.append (random.randint (0, 100))

    return (list)


def main ():

    SIZE = 10
    data = create_list (SIZE);
    sorted_data = sorted(data)
    print (sorted_data)
    target = int (input ("Number to find: "))
    found = recursive_binary_search (sorted_data, target, 0, len(data) - 1)
    print ("The recursive method found: " + str (found))
    found = iterative_binary_search (sorted_data, target, 0, len(data) - 1)
    print ("The iterative method found: " + str (found))


if __name__ == "__main__":
    main ()
