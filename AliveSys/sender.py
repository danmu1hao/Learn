import time
import socket
import json
from datetime import datetime

# 发送者配置
# 送信者の設定
HOST = 'localhost'
PORT = 12345
HEARTBEAT_INTERVAL = 5  # 心跳间隔（秒）
# ハートビート間隔（秒）
LIFETIME = 20 # 生命周期（秒）
# ライフタイム（秒）

def send_heartbeat():
    # 发送者：每5秒发送心跳信息，20秒后停止
    # 送信者：5秒ごとにハートビートを送信し、20後に停止します
    
    # 创建 UDP socket
    # UDP ソケットを作成します
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    start_time = time.time()
    
    try:
        while (time.time() - start_time) < LIFETIME:
            # 创建心跳消息
            # ハートビートメッセージを作成します
            message = {
                "type": "heartbeat",
                "timestamp": datetime.now().isoformat(),
                "message": "我还活着"
            }
            
            # 发送消息
            # メッセージを送信します
            data = json.dumps(message).encode('utf-8')
            sock.sendto(data, (HOST, PORT))
            
            print(f"[发送者] 发送心跳: {message['message']} - 时间: {message['timestamp']}")
            
            # 等待心跳间隔
            # ハートビート間隔を待機します
            time.sleep(HEARTBEAT_INTERVAL)
            
    except Exception as e:
        print(f"[发送者] 发送错误: {e}")
    finally:
        sock.close()
        print("[发送者] 发送者已停止")

if __name__ == "__main__":
    print("=== 心跳发送者启动 ===")
    print("=== ハートビート送信者開始 ===")
    print(f"目标地址: {HOST}:{PORT}")
    print(f"心跳间隔: {HEARTBEAT_INTERVAL}秒")
    print(f"生命周期: {LIFETIME}秒")
    print(" * " * 30)
    send_heartbeat() 