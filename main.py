import os
import shutil
import sys
import argparse
from pathlib import Path
from convert import convert_cursors
from mapper import convert_filenames
from symlinks import add_missing_xcursor
from clickgen.packer import pack_x11
from renamer import rename_files_with_strings

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert Windows cursors to X11 cursors.")
    parser.add_argument("-i", "--input", type=str, help="Input folder path.")
    parser.add_argument("-o", "--output", type=str, help="Output folder path, default to output folder under input folder.", default=None)
    parser.add_argument("-n", "--name", type=str, help="Name of the cursor pack")
    parser.add_argument("-s", "--size", type=int, help="The size of the converted cursor pack (equal width and height)", default=0)
    return parser.parse_args()

def main(input_folder_a, output_folder_b, name, size):
    # 创建临时文件夹/tmp
    tmp_folder = os.path.join(input_folder_a, "tmp")
    os.makedirs(tmp_folder, exist_ok=True)

    cursor_folder = os.path.join(output_folder_b, "cursors")
    if not os.path.exists(cursor_folder):
        os.makedirs(cursor_folder)

    try:
        # 步骤0: 根据 inf 文件重命名指针名称
        rename_files_with_strings(input_folder_a)

        # 步骤1：调用convert.py中的convert_cursors方法
        convert_cursors(input_folder_a, tmp_folder, size)

        # 步骤2：调用mapper.py中的convert_filenames方法
        convert_filenames(tmp_folder, cursor_folder)

        # 步骤3：删除临时文件夹/tmp及其中的文件
        shutil.rmtree(tmp_folder)

        # 步骤4：调用symlinks.py中的add_missing_xcursor方法
        # print(cursor_folder)
        add_missing_xcursor(cursor_folder)
        
        pack_x11(Path(output_folder_b), name, f"{name} Cursors")

        print("完成所有操作。")
    except Exception as e:
        print(f"发生错误：{e}")
        # 如果发生错误，确保删除临时文件夹/tmp及其中的文件
        # shutil.rmtree(tmp_folder)

if __name__ == "__main__":

    args = parse_arguments()
    input_folder_a = args.input

    if args.output is None:
        output_folder_b = os.path.join(input_folder_a, "output")
    else:
        output_folder_b = args.output

    name = args.name
    size = args.size

    output_folder_b = os.path.join(output_folder_b, name)

    if not os.path.exists(output_folder_b):
        os.makedirs(output_folder_b)    

    # 调用主函数
    main(input_folder_a, output_folder_b, name, size)
