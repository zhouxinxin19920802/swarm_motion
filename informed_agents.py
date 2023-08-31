# encoding:utf-8

# 读取数据
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
