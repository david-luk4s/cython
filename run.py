from timeit import timeit

cy = timeit(
    'fib(93)',
    number=1_000_000,
    setup='from fib_py import fib'
)

print(f'Cython puro: {cy}')