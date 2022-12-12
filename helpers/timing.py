from functools import wraps
from time import perf_counter_ns


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = perf_counter_ns()
        result = f(*args, **kw)
        te = perf_counter_ns()
        print(f"func: {f.__name__}, took: {(te-ts) / 1_000_000:.2f}ms")
        return result

    return wrap
