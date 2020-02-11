# 入力
n = 5,
s = [1,2,4,6,8] # 各タスクの開始時間
t = [3,5,7,9,10] # 各タスクの終了時間

# 選べる仕事の中で，終了時間が最も早いものを選ぶことを繰り返す
current_time = 0 # 現在の時刻

# import ipdb; ipdb.set_trace()
# 選べる仕事 -> 現在時刻よりも開始時間が先のもの
feasible_task = [[es, et] for es, et in zip(s, t) if es >= current_time]

# 実行する仕事のリスト
Todo = []

while feasible_task:
    # 最も終了時間が早いもの -> 上の中で終了時間が最も小さい
    todo = feasible_task[0]
    for i in range(len(feasible_task)-1):
        if todo[1] > feasible_task[i+1][1]:
            todo = feasible_task[i+1]
    Todo.append(todo)
    current_time = todo[1]
    feasible_task = [[es, et] for es, et in zip(s, t) if es >= current_time]

print(Todo)