import math
import numpy as np

n,p = map(int, input().split())

# n個の1以上の整数a1,...,anが与えられる
# それぞれの値はわかっていないが全ての要素の積がPであることはわかっている
# a1,...,anの最大公約数として考えられるもののうち最も大きいものを求めてください

# -----------------
# 素数列挙
def make_prime_list(num):
    if num < 2:
        return []

    prime_list = [i for i in range(num+1)]
    prime_list[1] = 0
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0 :
            continue
        if prime > num_sqrt:
            break

    for non_prime in range(2*prime, num, prime):
        prime_list[non_prime] = 0
    
    return [prime for prime in prime_list if prime != 0]
# -----------------

# -----------------
# 素因数分解
def prime_factorization(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list(num_sqrt)

        dict_counter = {}
        for prime in prime_list:
            while num % prime == 0:
                if prime in dict_counter:
                    dict_counter[prime] += 1
                else:
                    dict_counter[prime] = 1
                num //= prime
        
        if num != 1:
            if num in dict_counter:
                dict_counter[num] += 1
            else:
                dict_counter[num] = 1

        return dict_counter
# -----------------

if n == 1:
    res = p
elif p == 1:
    res = 1
else:
    d = prime_factorization(p)
    pe = []
    for k, v in zip(d.keys(), d.values()):
        if v >= n:
            pe.append(k * (v // n))
    res = np.prod(pe)

print(res)