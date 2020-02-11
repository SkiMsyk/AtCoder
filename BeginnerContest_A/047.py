candies = list(map(int, input().split()))
flag = "No"
for i in range(3):
    for j in range(3):
        k = list({0,1,2} - {i, j})[0]
        if candies[i] + candies[j] == candies[k]:
            flag = "Yes"

print(flag)