N = int(input())
total = 0
largest_pop = 0
for _ in range(N):
    city, pop = input().split()
    pop = int(pop)
    total += pop
    if pop > largest_pop:
        largest_city = city
        largest_pop = pop

if (largest_pop / total) <= 0.5:
    print('atcoder')
else:
    print(largest_city)