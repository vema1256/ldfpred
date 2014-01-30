def make_printer(y):
    def printer(x):
        print x + y
    return printer