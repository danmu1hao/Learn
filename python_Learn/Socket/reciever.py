from operator import truediv
import socket

# 接收端配置
# 受信側の設定
HOST = '127.0.0.1'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("接收端启动，等待消息...")
# 受信側起動、メッセージ待機中...

while(1):
    data, addr = sock.recvfrom(100)
    print(f"收到: {data.decode('utf-8')} 来自 {addr}")

sock.close()
print("接收端结束")
# 受信側終了