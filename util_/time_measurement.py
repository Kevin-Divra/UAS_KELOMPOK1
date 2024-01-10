import functools
import time
class CodeTimer:
    def _init_(self, name=None):
        self.name = f"'{name}'" if name else ''
    def _enter_(self):
        self.start = time.perf_counter()
    def _exit_(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        self.took = (self.end - self.start) * 1000.0
        print(f"Code block {self.name} took: {self.took:.2f} ms")
def time_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000.0
        print(f"Finished '{func._name_}' in {run_time:.2f} ms")
        return result
    return wrapper