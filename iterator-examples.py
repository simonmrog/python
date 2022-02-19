class Fibonacci:
    def __init__(self, max):
        self.__max = max

    def __iter__(self):
        self.__count = 0
        self.__f0 = 0
        self.__f1 = 1
        return self

    def __next__(self):
        if self.__count == 0:
            self.__count += 1
            return self.__f0
        elif self.__count == 1:
            self.__count += 1
            return self.__f1
        elif self.__count <= self.__max:
            result = self.__f0 + self.__f1
            self.__f0 = self.__f1
            self.__f1 = result
            self.__count += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    n = int(input())
    fibonacci_series = Fibonacci(n)
    fibonacci_iterator = iter(fibonacci_series)

    for k in fibonacci_iterator:
        print(k)