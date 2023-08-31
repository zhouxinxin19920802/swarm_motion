# encoding:utf-8

# 读取数据

average_time_dependence = []
with open("swarm_motion_couzin/data/average_time_dependence.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() != "":
            average_time_dependence.append(line)


# print(spatial_correlation )

cons = 0 
for item in average_time_dependence:
    if item != "\n":
        cons = cons + float(item)

cons = cons / (len(average_time_dependence) - 1)
print(cons)
