from timeit import default_timer


def profile(times: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = default_timer()
            for _ in range(times):
                func(*args, **kwargs)
            end = default_timer()
            time = end - start
            print(f"Time: {time:.4f}s, {times}x | {time/times:.4f}s/time")

        return wrapper

    return inner
