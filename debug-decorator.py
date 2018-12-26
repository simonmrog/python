def debug (func):
    def wrapper (*args, **kwargs):
        #prints directly the name of the function func
        print("Function {.__name__}() called!".format (func))
        return (func (*args, **kwargs))
    return (wrapper)


@debug
def sum (a, b):
    return (a + b)


@debug
def pow2 (a):
    return (a * a)


def main ():
    a = 3
    b = 2
    print ("a + b: " + str(sum (3, 2)))
    print ("a^2: " + str(pow2 (a)))


if __name__ == "__main__":
    main ()
