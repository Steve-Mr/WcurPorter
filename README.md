# WcurPorter

## 功能
  
将 Windows 下的 .cur/.ani 格式的指针转换到 xcursor。

## 依赖

[win2xcur](https://github.com/quantum5/win2xcur)

## 使用方法

`python3 main.py <path/to/windows/curs> <output_path> <xcursor_pack_name>`

## 问题

尽管本项目已经尽力实现对 Windows 鼠标文件到 xcursor 的自动映射，但是由于各个 pack 中制作的鼠标文件类别可能不一致，当出现 xcursor 中需要的鼠标文件在源 pack 中没有对应文件时，需要根据提示修改 constants.py 中的对应关系。

## 致谢

本项目中代码参考了 [fuchsia-cursor](https://github.com/ful1e5/fuchsia-cursor) 中大量内容。