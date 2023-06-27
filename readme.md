QuickDrop
English [简体中文](./readme_cn.md)
A simple application can help you share your file in a moment

'''
usage: quickdrop [-h] [-t TIME] -P PATH [-p PORT]

options:
  -h, --help            show this help message and exit
  -t TIME, --time TIME  Share time,format:time+unit,available unit:s,m,h,d,default unit: s,inf means share forever,default time is 300s
  -P PATH, --path PATH  path of the file you'd like to share, support abs and rev path
  -p PORT, --port PORT  port of the service of share file, default port is randomly
'''