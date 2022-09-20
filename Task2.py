import time
import random
import contextlib
import inspect
import io


def Decorator2(func):
    count = 0

    def wrapper(*args, **kwargs):

        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*args, **kwargs)
        end = time.perf_counter()
        s = f.getvalue()
        # print(s)
        nonlocal count
        count += 1
        print("{} call {}  executed in {:.2f} millisec".format(func.__name__, count, 10 ** 6 * (end - start)))
        print("Name:\t\t{:<16}".format(func.__name__))
        print("Sign:\t\t{}".format(inspect.signature(func)))
        print("Arg:\t\t{}".format(inspect.signature(func)))

        print("Doc:\t\t{:>16}".format(inspect.getdoc(func)))
        print(f'Source:\t{inspect.getsource(func)}'.replace('\n', '\n\t'), end='\n')
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            func(*args, **kwargs)
        s = f.getvalue()
        for l in s.splitlines():
            print("\t" + l)

    return wrapper




