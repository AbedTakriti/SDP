import time
import contextlib
import inspect
from prettytable import PrettyTable

rank = {}

class Decorator3:
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.time = 0

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        with open('Function_dump.txt', 'a') as q:
            with contextlib.redirect_stdout(q):
                output = self.func(*args, **kwargs)
                end = time.perf_counter()
                self.count += 1
                self.time = (10 ** 6 * (end - start))
                rank[self.func.__name__] = self.time
                print("{} call  {} executed in {:.2f} millisec".format(self.func.__name__, self.count, self.time))
                print("Name:\t\t{:<16}".format(self.func.__name__))
                print("Sign:\t\t{}".format(inspect.signature(self.func)))
                print("Arg:\t\t{}".format(args, kwargs))
                print("Source:\t\t{:>30}".format(inspect.getsource(self.func)))
                print("Output:\t\t{}".format(output))

        return output

def get_rank():
    sort_list = sorted(rank.items(), key=lambda x: x[1])
    sort_rank = dict(sort_list)
    t = PrettyTable(['Program', 'Rank', 'Time Elapsed'])
    i = 1
    for key, value in sort_rank.items():
        t.add_row([key, i, value])
        i += 1
    return t


def print_rank():
    with open('Function_dump.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            print("")
    t = get_rank()
    print(t)

