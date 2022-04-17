import cv2  # opencv lib
from socket import *  # socket lib
import numpy as np
'''
在下面输入你的IP地址.如果你是windows系统用户,你可以通过以下步骤获取你的IP:
1.确保你打开了电脑/笔记本的热点
2.Win+R并输入cmd打开命令行窗口
3.输出ipconfig,并在下面找到'本地连接'中获得你的IP
Write down your IP here.If you are a Windows system user,you can get your IP through following steps:
1.Make sure your computer/laptop's hotspot is open
2.Win+R and input 'cmd'         open the cmd window
3. input 'ipconfig',then find 'local area connection' to get your IP
'''
IP='XXX.XXX.XXX.XXX'
# 端口:可以在0-65535中间随意设置,确保你的服务器端和客户端使用相同的端口
# PORT:can be set among 0 to 65535.Make sure your server and client use the same PORT.
SEVER_PORT=50000
dataSocket=socket(AF_INET,SOCK_STREAM)
dataSocket.connect((IP,SEVER_PORT))
# 获取摄像头视频  get frame captured by webcam
cap = cv2.VideoCapture(0)
# 设置读入的图像大小 set your frame's size
cap.set(3,600)
cap.set(4,400)

while True:
    if(cap.isOpened()):  # 检验摄像头是否已经开启 make sure webcam is working 
     ret,frame = cap.read()
    img=cv2.imencode('.jpg',frame)[1]  # 使用opencv编码图片 using cv2 to encode picture
    data=np.array(img)
    str1=data.tobytes()
    encode_len=str(len(str1))
    flag_data=(encode_len).encode()+"end".encode()
    dataSocket.send(flag_data)
    str2=dataSocket.recv(1024)
    if "ok"==str2.decode():
       dataSocket.send(str1)
       recved=dataSocket.recv(1024)
       if "cancel"== recved.decode():  # 停止接收命令 cancel
         break
       print(recved.decode())
dataSocket.close()
