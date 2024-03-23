import os
import shutil
from constants import WIN_CURSORS_CFG

def convert_filenames(input_folder, output_folder):
    # 获取输入文件夹中的所有文件名
    files = os.listdir(input_folder)

    # 遍历文件并转换名称
    for file in files:
        file_lower = file.lower()
        if file_lower in map(str.lower, WIN_CURSORS_CFG.keys()):
            matching_keys = [key for key in WIN_CURSORS_CFG.keys() if key.lower() == file_lower]
            for new_name_key in matching_keys:
                new_names = WIN_CURSORS_CFG[new_name_key]
                if isinstance(new_names, list):  # 检查值是否为列表
                    for new_name in new_names:
                        input_path = os.path.join(input_folder, file)
                        output_path = os.path.join(output_folder, new_name)
                        shutil.copy2(input_path, output_path)  # 复制文件
                        # print(f"已将文件 '{file}' 复制为 '{new_name}' 并移动到输出文件夹。")
                else:
                    input_path = os.path.join(input_folder, file)
                    output_path = os.path.join(output_folder, new_names)
                    shutil.copy2(input_path, output_path)  # 复制文件
                    # print(f"已将文件 '{file}' 复制为 '{new_names}' 并移动到输出文件夹。")
        else:
            print(f"未找到文件 '{file}' 在 WIN_CURSORS_CFG 中的映射，将保持原文件名不变。")
