import os
import re
import chardet

def find_inf_file(input_path):
    # 遍历指定路径下的所有文件和文件夹
    for root, dirs, files in os.walk(input_path):
        for file in files:
            # 判断文件是否以 .inf 结尾
            if file.lower().endswith('.inf'):
                inf_file_path = os.path.join(root, file)
                return inf_file_path
    # 如果没有找到 .inf 文件，则返回 None
    return None

def detect_encoding(file_path):
    # 读取文件内容并检测编码
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    result = chardet.detect(rawdata)
    return result['encoding']

def parse_inf_file(inf_content):
    # 从.INF文件内容中提取Scheme.Cur中的对象和Strings中的对象
    scheme_cur = re.findall(r'"([^"]+\.ani)"', inf_content)
    strings = re.findall(r'(\w+)\s*=\s*"([^"]+)"', inf_content)

    # 构建Strings中的字典
    strings_dict = dict(strings)

    # 匹配Scheme.Cur中的对象名称与Strings中的值，并生成文件名
    file_names = []
    for obj in scheme_cur:
        for key, value in strings_dict.items():
            if value == obj:
                file_names.append((value, key))
                break

    return file_names

import os
import shutil

def rename_files_with_strings(input_path):
    inf_file = find_inf_file(input_path)

    if inf_file:
        # 自动检测编码
        encoding = detect_encoding(inf_file)
        
        # 读取 .inf 文件内容
        with open(inf_file, 'r', encoding=encoding) as file:
            inf_content = file.read()

        # 解析 .inf 文件内容
        file_names = parse_inf_file(inf_content)

        # 重命名文件
        for obj, file_name in file_names:
            old_file_path = os.path.join(input_path, obj)
            new_file_path = os.path.join(input_path, file_name + '.ani')
            if os.path.exists(old_file_path):
                if old_file_path != new_file_path:
                    shutil.copyfile(old_file_path, new_file_path)
                    print(f"复制文件: {old_file_path} -> {new_file_path}")
            else:
                print(f"文件不存在: {old_file_path}")

        # 创建或检查 bak 文件夹
        bak_folder = os.path.join(input_path, 'bak')
        if not os.path.exists(bak_folder):
            os.makedirs(bak_folder)

        # 将 old_file_path 中的所有文件移动到 bak 文件夹中
        for obj, _ in file_names:
            old_file_path = os.path.join(input_path, obj)
            if os.path.exists(old_file_path):
                shutil.move(old_file_path, bak_folder)
                print(f"移动文件到 bak 文件夹: {old_file_path}")

    else:
        print("未找到 .inf 文件")


# # 测试代码
# input_path = input("请输入要搜索的路径: ")
# rename_files_with_strings(input_path)
