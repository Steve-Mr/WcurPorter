import os
import subprocess
import glob
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from threading import Lock
from typing import BinaryIO

from win2xcur.parser import open_blob
from win2xcur import scale, shadow
from win2xcur.parser import open_blob
from win2xcur.writer import to_x11

def convert_cursors(input_folder, output_folder, size):
    # 处理输入文件夹和输出文件夹参数中最后是否有 "/" 的情况
    input_folder = input_folder.rstrip("/") + "/"
    output_folder = output_folder.rstrip("/") + "/"

    # convert_filetype(input_folder, output_folder, size, "cur")
    # convert_filetype(input_folder, output_folder, size, "ani")    
    convert_directly(input_folder, output_folder, size, "cur")
    convert_directly(input_folder, output_folder, size, "ani")

def convert_filetype(input_folder, output_folder, size, type):
    files = [file for file in os.listdir(input_folder) if file.endswith(type)]
    if files:
        scale = get_scale(os.path.join(input_folder, files[0]), size)

        # 构建命令字符串
        command_cur = f"win2xcur {input_folder}*.{type} -o {output_folder} --scale {scale}"

        # 执行第二个命令
        print("开始执行命令:", command_cur)
        subprocess.run(command_cur, shell=True, check=True)
        print("第二个命令执行完成！")
    else:
        print(f"输入文件夹中不存在 .{type} 格式的文件！")

def convert_directly(input_folder, output_folder, size, type):
    def process(file_path: str) -> None:
        try:
            # Read the file content directly
            with open(file_path, 'rb') as file:
                blob = file.read()
                cursor = open_blob(blob)
        except Exception as e:
            print(e)
        else:
            scale_ = get_scale(os.path.join(input_folder, files[0]), size)
            if scale_ != 1:
                scale.apply_to_frames(cursor.frames, scale=scale_)
            result = to_x11(cursor.frames)
            output = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0])
            with open(output, 'wb') as f:
                f.write(result)

    files = [os.path.join(input_folder,file) for file in os.listdir(input_folder) if file.endswith(type)]
    with ThreadPool(cpu_count()) as pool:
        pool.map(process, files)

def get_scale(target_file, size):
    try:
        if (size == 0):
            return 1 
        with open(target_file, "rb") as f:
            cursor = open_blob(f.read())
            orig_size = cursor.frames[0][0].image.width
            scale = int(size) / orig_size
            return scale
    except Exception as e:
        print(f"获取文件 {target_file} 的 scale 值时出错：{e}")
        return None
# # 示例调用
# input_folder = "/path/to/input_folder/"
# output_folder = "/path/to/output_folder/"
# convert_cursors(input_folder, output_folder)
