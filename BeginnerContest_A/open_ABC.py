import webbrowser
num, prob = input().split()
url = 'https://atcoder.jp/contests/abc' + num + "/tasks/abc" + num + "_" + prob
webbrowser.open_new_tab(url)

# ABCは019まで問題を表す末尾が_1, _2 だが
# 020からは末尾が _a, _b と変更されている