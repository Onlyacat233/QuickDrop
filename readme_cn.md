QuickDrop
[English](./readme.md) 简体中文

这个程序可以快速创建文件分享服务器

'''
usage: quickdrop [-h] [-t TIME] -P PATH [-p PORT]

选项:
  -h, --help            显示帮助信息后退出
  -t TIME, --time TIME  分享时间,形式:时长+单位,可选单位:s,m,h,d,没有单位默认按照秒计算,若输入inf则代表一直分享,默认值300
  -P PATH, --path PATH  分享文件路径,支持绝对路径和相对路径
  -p PORT, --port PORT  分享文件端口,默认随机
'''