import socket
from flask import Flask, send_file
import multiprocessing
from random import randint
from time import sleep
import argparse, os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def getTime(rawTime: str) -> int:
    """
    查询分享时间
    :return: time
    """

    if rawTime == "inf":
        return -1

    if is_number(rawTime):
        secTime = int(rawTime)
    else:
        time = int(rawTime[:-1])
        unit = rawTime[-1]

        if unit == 's':
            secTime = time
        elif unit == 'm':
            secTime = 60 * time
        elif unit == 'h':
            secTime = 3600 * time
        elif unit == 'd':
            secTime = 24 * 3600 * time
        else:
            secTime = 300
    
    return secTime


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()

    return ip

def endShare(shareProcess: multiprocessing.Process, time: int) -> None:
    sleep(time)
    print("分享结束")
    shareProcess.terminate()
    exit(0)

def getArgs():
    parser = argparse.ArgumentParser(description="这个程序可以快速创建文件分享服务器")
    parser.add_argument('-t', '--time', dest='time', type=str, default=300,   help="分享时间,形式:时长+单位,可选单位:s,m,h,d,没有单位默认按照秒计算,若输入inf则代表一直分享,默认值300")
    parser.add_argument('-P', '--path', dest='path', type=str, required=True, help="分享文件路径,支持绝对路径和相对路径")
    parser.add_argument('-p', '--port', dest='port', type=int, default=randint(50000, 60000),  help="分享文件端口,默认随机")

    args = parser.parse_args()

    return args

app = Flask(__name__)

@app.route('/')
def awa():
    return send_file(filepath)
    
try:
    if __name__ == "__main__":

        args = getArgs()

        ip = get_host_ip()
        filepath = os.path.abspath(args.path)
        port = args.port
        time = getTime(args.time)

        print(f"分享在: http://{ip}:{port}")

        shareProcess = multiprocessing.Process(target=app.run, kwargs={"port": port, "host": "0.0.0.0"})
        shareProcess.start()

        if time != -1:
            multiprocessing.Process(target=endShare, kwargs={"shareProcess": shareProcess, "time": time}).start()

except InterruptedError:
    endShare(shareProcess=shareProcess, time=0)
except Exception as e:
    print(f"分享错误: {e}")