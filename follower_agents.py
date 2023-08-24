
# encoding:utf-8

# 读取数据

follower_agents = []
with open("swarm_motion_couzin/data/follower_agents.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() != "":
           follower_agents.append(line)


# print(spatial_correlation )

cons = 0 
for item in follower_agents:
    if item != "\n":
        cons = cons + float(item)

cons = cons / (len(follower_agents) - 1)
print(cons)
