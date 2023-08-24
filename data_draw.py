# encoding:utf-8

# 读连通度
connectivitys = []

with open("swarm_motion_couzin/data/swarm_connectity.txt", "r") as f:
    lines = f.readlines()
    connectivity = []
    for line in lines:
        print(line)
        connectivity.append(line)
        if line.strip() == "":
            connectivitys.append(connectivity)
            connectivity = []
    # print(connectivitys)


print("##########################")
# 判断最后一次是否完整结束
if len(connectivitys[-1]) != len(connectivitys[0]):
    connectivitys.pop()

# 相同位置的数值相加取平均值
data_presentatiion = [0] * (len(connectivitys[0])-1)
for swarm_connect_index in range(len(data_presentatiion)):
    for item in connectivitys:
        if item != "\n":
            data_presentatiion[swarm_connect_index] = data_presentatiion[swarm_connect_index] + float(item[swarm_connect_index].rstrip("\n"))
    data_presentatiion[swarm_connect_index] = data_presentatiion[swarm_connect_index] / len(connectivitys)


# matplotlib 绘图
import matplotlib.pyplot as plt 
import numpy as np

# x 轴
x = np.arange(0,len(data_presentatiion),1)

plt.plot(x, data_presentatiion, color = "red",marker = "o", linestyle = "dashed")

plt.xlabel("Steps")
plt.ylabel("Swarm_connectivity")

plt.show()