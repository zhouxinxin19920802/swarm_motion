# encoding:utf-8

# 读取数据

spatial_correlation = []
with open("swarm_motion_couzin/data/spatial_correlation.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() != "":
           spatial_correlation.append(line)


# print(spatial_correlation )

cons = 0 
for item in spatial_correlation:
    if item != "\n":
        cons = cons + float(item)

cons = cons / (len(spatial_correlation) - 1)
print(cons)
