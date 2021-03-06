# 私たちは、新聞の購読に関する調査を行いました。 具体的には、調査の対象者 N 人に対し、それぞれ次の 2 つの質問を行いました。

# 質問 1: あなたは新聞 X を購読しているか？
# 質問 2: あなたは新聞 Y を購読しているか？
# その結果、質問 1 に対して「はい」と回答した人の数は A 人、質問 2 に対して「はい」と回答した人の数は B 人でした。

# このとき、調査の対象者のうち新聞 X, Y の両方を購読している人の数は最大で何人であり、また最小で何人であると考えられるでしょうか？

# この問いに答えるプログラムを書いてください。

n, a, b = map(int, input().split())
commonMax = min(a,b)
if a + b < n:
    commonMin = 0
else:
    commonMin = (a + b) - n

print(commonMax, commonMin)