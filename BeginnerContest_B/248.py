# Slimes
import math
A,B,K = map(int, input().split())

print(math.ceil(math.log10(B/A)/math.log10(K)))