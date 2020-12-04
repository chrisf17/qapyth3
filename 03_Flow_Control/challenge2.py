def generate_numbers(start, stop, step = 1):
    count = start
    while count < stop:
        yield count
        count += step

def primes(count):
    pass

def fibonacci(count):
    pass

for num in generate_numbers(0, 20):
    print(num)