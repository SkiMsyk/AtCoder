# 問題文
# 以下を満たす整数をすべて昇順に出力してください。

# A 以上 B 以下の整数の中で、小さい方から K 番目以内であるか、大きい方から K 番目以内である
# 制約
# 1≤A≤B≤109
# 1≤K≤100
# 入力はすべて整数である

a, b, k = map(int, input().split())

res = set()

for i in range(a, a+k):
    if i <= b:
        res.add(i)

for i in range(b-k+1, b+1):
    if a <= i:
        res.add(i)

# print(res)

for i in sorted(list(res)):
    print(i)