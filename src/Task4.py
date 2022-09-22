import time
import contextlib
import inspect
from prettytable import PrettyTable
import logging
rank = {}

LOG_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(
    filename="C:\\Users\\Abdulrahman Takriti\\PycharmProjects\\pythonProject1\\pythonProject\\Assignment1\\Error_log.log" \
    , level=logging.NOTSET, format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

def task3_functionality():
    sort_list = sorted(rank.items(), key=lambda x: x[1])
    sort_rank = dict(sort_list)
    t = PrettyTable(['Program', 'Rank', 'Time Elapsed'])
    i = 1
    for key, value in sort_rank.items():
        t.add_row([key, i, value])
        i += 1

    print(t)

class Decorator4:
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.time = 0

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        output = None
        with open('Function_dump.txt', 'a') as f:
            with contextlib.redirect_stdout(f):
                try:
                    output = self.func(*args, **kwargs)
                except:
                    with open('Error_log.log', 'w') as e:
                        with contextlib.redirect_stdout(e):

                            print("Error Message")

        end = time.perf_counter()
        self.count += 1
        self.time = (10 ** 6 * (end - start))
        rank[self.func.__name__] = self.time
        with open('Function_dump.txt','a') as f:
            with contextlib.redirect_stdout(f):

                print("{} call  {} executed in {:.2f} millisec".format(self.func.__name__, self.count, self.time))
                print("Name:\t\t{:<16}".format(self.func.__name__))
                print("Sign:\t\t{}".format(inspect.signature(self.func)))
                print("Arg:\t\t{}".format(args, kwargs))
                # print("Doc:\t\t{:>16}".format(inspect.getdoc(self.func)))
                print("Source:\t\t{:>30}".format(inspect.getsource(self.func)))
                print("Output:\t\t{}".format(output))

        task3_functionality()
        return output
