from timeit import default_timer
import timeit


def profile(number: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            def run():
                func(*args, **kwargs)

            time = timeit.timeit("run()", globals=locals(), number=number)
            print(f"Time: {time:.4f}s, {number}x | {time/number:.4f}s/time")

        return wrapper

    return inner
