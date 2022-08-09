from fractions import Fraction
list_price, sales_price = map(int, input().split())
ans = 1 - Fraction(sales_price, list_price)
print(float(ans)*100)