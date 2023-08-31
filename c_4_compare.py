# encoding:utf-8

# test4.html 
# E:\\zhouxin\\swarm_motion\\data\\swarm_connectity.txt"

# testc.html
# "E:\\zhouxin\\swarm_motion\\swarm_motion_couzin\\data\\swarm_connectity.txt"


# 集群连通度
def Swarm_connectivity_cal(path):

    connectivitys = []
    with open(path, "r") as f:
        lines = f.readlines()
        connectivity= [] 
        for line in lines:
            connectivity.append(line)
            if line.strip() == "":
                connectivitys.append(connectivity)
                connectivity = []
 


    print("##########################")

    # 判断最后一次是否完整结束
    if len(connectivitys[-1]) != len(connectivitys[0]):
        connectivitys.pop()

    # 相同位置的数值相加取平均值
    data_presentatiion = [0] * (len(connectivitys[0])-1)

    for swarm_connect_index in range(len(data_presentatiion)):
        for item in connectivitys:
            if item != "\n":
                # print(item[swarm_connect_index],item[swarm_connect_index].rstrip("\n"))
                data_presentatiion[swarm_connect_index] = data_presentatiion[swarm_connect_index] + float(item[swarm_connect_index].rstrip("\n"))
        data_presentatiion[swarm_connect_index] = data_presentatiion[swarm_connect_index] / len(connectivitys)

    return data_presentatiion


# matplotlib 绘图
import matplotlib.pyplot as plt 
import numpy as np

test4 = "data/swarm_connectity.txt"
data_presentation_4 = Swarm_connectivity_cal(test4)

testc = "swarm_motion_couzin/data/swarm_connectity.txt"
data_presentation_c = Swarm_connectivity_cal(testc)

tests = "swarm_motion_couzin/data/swarm_connectity_s.txt"
data_presentation_s = Swarm_connectivity_cal(testc)

# 空间相关度
def spatial_correlation_cal(path):
    spatial_correlation = []
    with open(path, "r") as f:
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
    return cons

test4 = "data/spatial_correlation.txt"
Swarm_connectivity_4 = Swarm_connectivity_cal(test4)

testc = "swarm_motion_couzin/data/spatial_correlation.txt"
Swarm_connectivity_c = Swarm_connectivity_cal(testc)

tests = "swarm_motion_couzin/data/spatial_correlation_s.txt"
Swarm_connectivity_s = Swarm_connectivity_cal(tests)

print("swarm_connectivity:",Swarm_connectivity_4,Swarm_connectivity_c, Swarm_connectivity_s)

# 时间相关度
def time_destination():
    average_time_dependence = []
    with open("swarm_motion_couzin/data/average_time_dependence.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() != "":
                average_time_dependence.append(line)
    cons = 0 
    for item in average_time_dependence:
        if item != "\n":
            cons = cons + float(item)

    cons = cons / (len(average_time_dependence) - 1)
    return cons

test4 = "data/average_time_dependence.txt"
average_time_dependence_4 = Swarm_connectivity_cal(test4)

testc = "swarm_motion_couzin/data/average_time_dependence.txt"
average_time_dependence_c = Swarm_connectivity_cal(testc)

tests = "swarm_motion_couzin/data/average_time_dependence_s.txt"
average_time_dependence_s = Swarm_connectivity_cal(tests)

print("average_time_dependence:",average_time_dependence_4,average_time_dependence_c, average_time_dependence_s)

print(average_time_dependence_4,average_time_dependence_c, average_time_dependence_s)

# 到达终点的知情者个数
def data_read_average(path):
    data = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() != "":
                data.append(line)
    # print(spatial_correlation )

    cons = 0 
    for item in data:
        if item != "\n":
            cons = cons + float(item)

    cons = cons / (len(data) - 1)
    return cons

test4 = "data/informed_agents.txt"
informed_agents_4= data_read_average(test4)

testc = "swarm_motion_couzin/data/informed_agents.txt"
informed_agents_c = data_read_average(testc)

tests = "swarm_motion_couzin/data/informed_agents_s.txt"
informed_agents_s = data_read_average(tests)

print("informed_agents:",informed_agents_4,informed_agents_c, informed_agents_s)


# 追随者个数
test4 = "data/follower_agents.txt"
follower_agents_4= data_read_average(test4)

testc = "swarm_motion_couzin/data/follower_agents.txt"
follower_agents_c = data_read_average(testc)

tests = "swarm_motion_couzin/data/follower_agents_s.txt"
follower_agents_s = data_read_average(tests)

print("follower_agents:",follower_agents_4,follower_agents_c, follower_agents_s)

# 到达的时间
test4 = "data/time_destination.txt"
follower_agents_4= data_read_average(test4)

testc = "swarm_motion_couzin/data/time_destination.txt"
follower_agents_c = data_read_average(testc)

tests = "swarm_motion_couzin/data/time_destination_s.txt"
follower_agents_s = data_read_average(tests)

print("time_destination:",follower_agents_4,follower_agents_c, follower_agents_s)





# x = np.arange(0,len(data_presentation_4),1)
# plt.plot(x, data_presentation_4, color = "purple", marker = ".", label = "4")
# plt.plot(x, data_presentation_c, color = "green", marker = "v", label = "c")
# plt.plot(x, data_presentation_s, color = "red", marker = "1", label = "s")



# plt.ylim(0,1)
# plt.legend()
# plt.show()