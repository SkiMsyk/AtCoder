# Weather Prediction
S = input()
tenki = ['Sunny', 'Cloudy', 'Rainy']
tomorrow = ((tenki.index(S) + 1) % 3)
print(tenki[tomorrow])

