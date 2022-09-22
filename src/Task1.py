import time
import contextlib
import io


def Decorator1(func):
    count = 0

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            result=func(*args, **kwargs)
        end = time.perf_counter()
        nonlocal count
        count += 1
        print("{} call {}  executed in {:.2f} millisec".format(func.__name__, count, 10 ** 6 * (end - start)))
        return result

    return wrapper




