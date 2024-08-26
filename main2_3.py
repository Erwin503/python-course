def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = [i for i in numbers if isPrime(i)]
not_primes = [i for i in numbers if not isPrime(i)]

print(f"Prime numbers: {primes}")
print(f"Non prime numbers: {not_primes}")