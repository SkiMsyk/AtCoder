# input
n = 6
r = 10
x = [1,7,15,20,30,50]

# 方針: 一番左の点から最もr以内の遠い点に印をつける
#   - 印をつけた点から右にR以上離れている次の点について
#     そこから距離r以内の最も遠い点に印をつける
#   - 全ての点xをカバーできたらそこで終了

lowest_value = 0
new_mark = 0
new_marks = []
cover_area = [0,0]

# import ipdb; ipdb.set_trace()
check = [True if cover_area[0] <= e and e <= cover_area[1] else False for e in x ]
while sum(check) != len(check):
    if cover_area[1] == 0:
        new_mark = 10
    else:
        new_mark = cover_area[1] + 1 + 10
    new_marks.append(new_mark)
    cover_area[1] = new_mark + 10
    check = [True if cover_area[0] <= e and e <= cover_area[1] else False for e in x ]

print(new_marks)
print(cover_area)