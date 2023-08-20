

import os
import os

def clear_folder(folder_path):
    # 获取目标文件夹中的所有文件名
    files = os.listdir(folder_path)

    # 删除每个文件
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            import shutil
            shutil.rmtree(file_path)

# 使用示例：清空名为 "target_folder" 的文件夹
target_folder = "data"
clear_folder(target_folder)
target_folder_contrast= "swarm_motion_couzin/data"
clear_folder(target_folder_contrast)