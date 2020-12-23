# count = 20
#
# i = 0
# while i < count:
#     print(count)
#     count += 1

# Primes
count = 20
generated = 0
prime = 1
while generated < count:
    if not any([i for i in (2,3,5,7,11) if prime % i == 0 and prime != i]):
        print(prime)
        generated += 1
    prime += 1


# fibonacci
count = 20
first, second = 0, 1
print(first)
print(second)

generated = 2
while generated <= count:
    fib_n = first + second
    print(fib_n)
    first, second = second, fib_n
    generated += 1

