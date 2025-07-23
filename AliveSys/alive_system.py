import threading
import time
import queue
from queue import Queue
from datetime import datetime

# 创建队列用于线程间通信
# スレッド間通信のためのキューを作成します
alive_queue = Queue()

# 全局标志用于控制线程
# スレッド制御のためのグローバルフラグ
running = True

def sender():
    """
    发送者：每5秒发送心跳信息，20秒后停止
    送信者：5秒ごとにハートビートを送信し、20秒後に停止します
    """
    global running
    start_time = time.time()
    
    while running and (time.time() - start_time) < 20:
        # 发送心跳信息
        # ハートビートメッセージを送信します
        message = f"我还活着 - 时间: {datetime.now().strftime('%H:%M:%S')}"
        alive_queue.put(message)
        print(f"[发送者] {message}")
        
        # 等待5秒
        # 5秒待機します
        time.sleep(5)
    
    # 20秒后停止发送
    # 20秒後に送信を停止します
    print("[发送者] 发送者已停止")
    running = False

def receiver():
    """
    接收者：检查心跳信息，如果10秒没收到则报警
    受信者：ハートビートメッセージをチェックし、10秒間受信しなければアラートを出します
    """
    global running
    last_heartbeat = time.time()
    
    while running:
        try:
            # 尝试从队列获取消息，超时10秒
            # キューからメッセージを取得しようとし、10秒でタイムアウトします
            message = alive_queue.get(timeout=10)
            last_heartbeat = time.time()
            print(f"[接收者] 收到: {message}")
            
        except queue.Empty:
            # 10秒内没有收到消息
            # 10秒以内にメッセージを受信しませんでした
            current_time = time.time()
            if current_time - last_heartbeat >= 10:
                print(f"[接收者] 警告！已经 {int(current_time - last_heartbeat)} 秒没有收到心跳信息")
                print("[接收者] 发送者可能出问题了！")
                break
    
    print("[接收者] 接收者已停止")

def main():
    """
    主函数：启动发送者和接收者线程
    メイン関数：送信者と受信者のスレッドを開始します
    """
    print("=== 心跳系统启动 ===")
    print("=== ハートビートシステム開始 ===")
    
    # 创建线程
    # スレッドを作成します
    sender_thread = threading.Thread(target=sender, name="Sender")
    receiver_thread = threading.Thread(target=receiver, name="Receiver")
    
    # 启动线程
    # スレッドを開始します
    sender_thread.start()
    receiver_thread.start()
    
    # 等待线程结束
    # スレッドの終了を待機します
    sender_thread.join()
    receiver_thread.join()
    
    print("=== 心跳系统结束 ===")
    print("=== ハートビートシステム終了 ===")

if __name__ == "__main__":
    main() 