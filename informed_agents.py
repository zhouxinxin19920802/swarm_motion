# encoding:utf-8

# 读取数据

infomred_agents = []
with open("swarm_motion_couzin/data/informed_agents.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() != "":
           infomred_agents.append(line)


# print(spatial_correlation )

cons = 0 
for item in infomred_agents:
    if item != "\n":
        cons = cons + float(item)

cons = cons / (len(infomred_agents) - 1)
print(cons)
