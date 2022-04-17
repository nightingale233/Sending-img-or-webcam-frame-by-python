from socket import *
import cv2
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
PORT=50000
# 接收的字节数 最大值 2147483647 （31位的二进制）
BUFLEN=2147483647
listenSocket = socket(AF_INET,SOCK_STREAM)
listenSocket.bind((IP,PORT))
# 设置最大的监听数,默认为1 set maximum listening clients
listenSocket.listen(1)
print(f'服务器启动成功，在{PORT}端口等待客户端连接。。。')
dataSocket,addr=listenSocket.accept()
print('接受一个客户端连接:',addr)
while True:
    receive_encode = dataSocket.recv(BUFLEN)
    nparr = np.frombuffer(receive_encode, np.uint8)  # 转化为numpy change to numpy form
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # 图像解码 img decode
    cv2.imshow("Client_show", img_decode)
    c=cv2.waitKey(10)
    if c&0xFF == 'q':  
      dataSocket.send('cancel'.encode())
      break
    else:
      dataSocket.send('服务端接收到了信息'.encode())
cv2.destroyWindow("Client_show")
dataSocket.close()
listenSocket.close()
