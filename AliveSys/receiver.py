import socket
import json
import time
from datetime import datetime

# 接收者配置
# 受信者の設定
HOST = 'localhost'
PORT = 12345
TIMEOUT = 10  # 超时时间（秒）
# タイムアウト時間（秒）

def receive_heartbeat():
    # 接收者：检查心跳信息，如果10秒没收到则报警
    # 受信者：ハートビートメッセージをチェックし、10秒間受信しなければアラートを出します
    
    # 创建 UDP socket
    # UDP ソケットを作成します
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    sock.settimeout(TIMEOUT)
    
    last_heartbeat = time.time()
    
    print(f"[接收者] 开始监听 {HOST}:{PORT}")
    print(f"[接收者] 超时时间: {TIMEOUT}秒")
    
    try:
        while True:
            try:
                # 接收消息
                # メッセージを受信します
                data, addr = sock.recvfrom(1024)
                message = json.loads(data.decode('utf-8'))
                
                last_heartbeat = time.time()
                print(f"[接收者] 收到来自 {addr} 的心跳: {message['message']} - 时间: {message['timestamp']}")
                
            except socket.timeout:
                # 超时检查
                # タイムアウトチェック
                current_time = time.time()
                elapsed = current_time - last_heartbeat
                
                if elapsed >= TIMEOUT:
                    print(f"[接收者] 警告！已经 {int(elapsed)} 秒没有收到心跳信息")
                    print("[接收者] 发送者可能出问题了！")
                    break
                else:
                    print(f"[接收者] 等待中... ({int(elapsed)}秒)")
                    
    except KeyboardInterrupt:
        print("\n[接收者] 用户中断")
    except Exception as e:
        print(f"[接收者] 接收错误: {e}")
    finally:
        sock.close()
        print("[接收者] 接收者已停止")

if __name__ == "__main__":
    print("=== 心跳接收者启动 ===")
    print("=== ハートビート受信者開始 ===")
    print(f"监听地址: {HOST}:{PORT}")
    print(f"超时时间: {TIMEOUT}秒")
    print("=" * 30)
    receive_heartbeat() 