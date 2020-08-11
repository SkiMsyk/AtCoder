import webbrowser
num, prob = input().split()
url = 'https://atcoder.jp/contests/abc' + num + "/tasks/abc" + num + "_" + prob
webbrowser.open_new_tab(url)