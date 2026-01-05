import time


def timer(function):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = function(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{function.__name__} running time: {run_time:.8f}")
        return value

    return wrapper_timer