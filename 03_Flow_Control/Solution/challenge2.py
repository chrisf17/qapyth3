def generate_numbers(start, stop, step = 1):
    count = start
    while count < stop:
        yield count
        count += step

def primes(count):

    generated = 0
    prime = 1
    while generated < count:
        if not any([i for i in (2,3,5,7,11) if prime % i == 0 and prime != i]):
            yield prime
            generated += 1
        prime += 1


def fibonacci(count):

    first, second = 0, 1

    if count < 1:
        raise ValueError("A minimum count of 1 is required")

    if count >= 1:
        yield first

    if count >= 2:
        yield second

    generated = 2
    while generated <= count:
        fib_n = first + second
        yield fib_n
        first, second = second, fib_n
        generated += 1

# for num in generate_numbers(0, 20):
#     print(num)

for num in primes(20):
    print(num)