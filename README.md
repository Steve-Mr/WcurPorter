# WcurPorter

## 功能
  
将 Windows 下的 .cur/.ani 格式的指针转换到 xcursor。

## 使用方法

### 安装
```sh
pip install -e git+https://github.com/quantum5/win2xcur.git#egg=win2xcur
pip install chardet clickgen numpy
```
`git clone https://github.com/Steve-Mr/WcurPorter.git`

### 使用
```
usage: main.py [-h] [-i INPUT] [-o OUTPUT] [-n NAME] [-s SIZE]

Convert Windows cursors to X11 cursors.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input folder path.
  -o OUTPUT, --output OUTPUT
                        Output folder path, default to output folder under input folder.
  -n NAME, --name NAME  Name of the cursor pack
  -s SIZE, --size SIZE  The size of the converted cursor pack (equal width and height)
```
示例：  
`python3 main.py -i /home/username/Downloads/yuuka -n yuuka -s 32`

## 问题

- 设置 size 参数效果可能出现预料外的问题
- 尽管本项目已经尽力实现对 Windows 鼠标文件到 xcursor 的自动映射，但是由于各个 pack 中制作的鼠标文件类别可能不一致，当出现 xcursor 中需要的鼠标文件在源 pack 中没有对应文件时，需要根据提示修改 constants.py 中的对应关系。

## 致谢

本项目基于[win2xcur](https://github.com/quantum5/win2xcur)，
部分代码参考了 [fuchsia-cursor](https://github.com/ful1e5/fuchsia-cursor) 。