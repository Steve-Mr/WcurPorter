import os
import shutil
import sys
from pathlib import Path
from convert import convert_cursors
from mapper import convert_filenames
from symlinks import add_missing_xcursor
from clickgen.packagers import XPackager
from renamer import rename_files_with_strings

def main(input_folder_a, output_folder_b, name):
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
        convert_cursors(input_folder_a, tmp_folder)

        # 步骤2：调用mapper.py中的convert_filenames方法
        convert_filenames(tmp_folder, cursor_folder)

        # 步骤3：删除临时文件夹/tmp及其中的文件
        shutil.rmtree(tmp_folder)

        # 步骤4：调用symlinks.py中的add_missing_xcursor方法
        # print(cursor_folder)
        add_missing_xcursor(cursor_folder)

        XPackager(Path(output_folder_b), name, f"{name} Cursors")

        print("完成所有操作。")
    except Exception as e:
        print(f"发生错误：{e}")
        # 如果发生错误，确保删除临时文件夹/tmp及其中的文件
        # shutil.rmtree(tmp_folder)

if __name__ == "__main__":
    # 检查命令行参数是否正确
    if len(sys.argv) != 4:
        print("请提供输入文件夹、输出文件夹和名称作为命令行参数。")
        print("用法: python main.py <input_folder_a> <output_folder_b> <name>")
        sys.exit(1)

    input_folder_a = sys.argv[1]
    output_folder_b = sys.argv[2]
    name = sys.argv[3]

    output_folder_b = os.path.join(output_folder_b, name)

    if not os.path.exists(output_folder_b):
        os.makedirs(output_folder_b)    

    # 调用主函数
    main(input_folder_a, output_folder_b, name)
