follower, followee = map(int, input().split())
followable_number = 2 * follower + 100
answer = followable_number - followee
print(answer)