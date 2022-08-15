cards = list(map(int, input().split()))
counts = [0]*13

# count up at card number position.
for card in cards:
    counts[card-1] += 1

pair = 0
three_card = 0
for count in counts:
    if count == 2:
        pair = 1
    if count == 3:
        three_card = 1

if pair and three_card:
    ans = "Yes"
else:
    ans = 'No'

print(ans)