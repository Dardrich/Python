n = int(input())
initial_robotval = list(map(int,input().split()))
robot_value = 0
tile_num = 0
total = 0
datas = []

for i in initial_robotval:
    if i == 1:
        robot_value += 1
        tile_num += 1
        if tile_num == n:
            if initial_robotval[0] == 1:
                robot_value = robot_value + datas[0]
                datas.pop(0)
            datas.append(robot_value)
    elif i == 0:
        datas.append(robot_value)
        robot_value = 0
        tile_num += 1
        
for i in datas:
    if i != 0:
        for j in range(i+1):
            total += j

print(total)



