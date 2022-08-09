from collections import deque
import math

# -----------------
# numに対する素数判定
def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3 or num ==4:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False

    prime = 7
    step = 4
    num_sqrt = math.sqrt(num)
    while prime <= num_sqrt:
        if num % prime == 0:
            return False
        prime += step
        step = 6 - step
    
    return True
# -----------------

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

# -----------------
# 約数の個数
def search_divisor_num(num):
    if num < 0:
        return None
    elif num == 1:
        return 1
    else:
        divisor_num = 1
        dict_fact = prime_factorization(num)
        for value in dict_fact.values():
            divisor_num *= (value + 1)
        return divisor_num
# -----------------

# -----------------
# 約数列挙
def make_divisor_list(num):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = deque()
        divisor_list.append(1)
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisor_list.append(i)
        divisor_list.append(num)

        return divisor_list
