import os
import subprocess


def convert_cursors(input_folder, output_folder):
    # 处理输入文件夹和输出文件夹参数中最后是否有 "/" 的情况
    input_folder = input_folder.rstrip("/") + "/"
    output_folder = output_folder.rstrip("/") + "/"

    # 构建命令字符串
    # command = f"win2xcur {input_folder}*.{{ani,cur}} -o {output_folder}"
    command_ani = f"win2xcur {input_folder}*.ani -o {output_folder}"
    command_cur = f"win2xcur {input_folder}*.cur -o {output_folder}"

    # 检查输入文件夹中是否存在 .ani 格式的文件
    ani_files = [file for file in os.listdir(input_folder) if file.endswith(".ani")]
    if ani_files:
        # 构建命令字符串
        command_ani = f"win2xcur {input_folder}*.ani -o {output_folder}"

        # 执行第一个命令
        print("开始执行命令:", command_ani)
        subprocess.run(command_ani, shell=True, check=True)
        print("第一个命令执行完成！")
    else:
        print("输入文件夹中不存在 .ani 格式的文件！")

    # 检查输入文件夹中是否存在 .cur 格式的文件
    cur_files = [file for file in os.listdir(input_folder) if file.endswith(".cur")]
    if cur_files:
        # 构建命令字符串
        command_cur = f"win2xcur {input_folder}*.cur -o {output_folder}"

        # 执行第二个命令
        print("开始执行命令:", command_cur)
        subprocess.run(command_cur, shell=True, check=True)
        print("第二个命令执行完成！")
    else:
        print("输入文件夹中不存在 .cur 格式的文件！")

# # 示例调用
# input_folder = "/path/to/input_folder/"
# output_folder = "/path/to/output_folder/"
# convert_cursors(input_folder, output_folder)
