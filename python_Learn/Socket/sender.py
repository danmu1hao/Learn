import socket
import time

# 发送端配置
# 送信側の設定
HOST = '127.0.0.1'  # 本地回环地址
# ローカルループバックアドレス
PORT = 12345        # 端口
# ポート番号

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(5):
    msg = f"第{i+1}次"
    # 第{i+1}回：こんにちは、受信側！
    sock.sendto(msg.encode('utf-8'), (HOST, PORT))
    print(f"已发送: {msg}")
    # 送信済み
    time.sleep(1)

sock.close()
print("发送端结束")
# 送信側終了