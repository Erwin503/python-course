def trap(n):
    res = ''
    for i in range(1, n // 2 + 1):
        for j in range(1, n - i + 1):
            print(f'{n} % ({i} + {j}) == 0 = {(n % (i + j)) == 0}')
            if (n % (i + j)) == 0:
                res += str(i) + str(j)

    return res

print(trap(8))