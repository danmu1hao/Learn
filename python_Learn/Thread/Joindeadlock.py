import threading
import time
import sys

class DeadlockThread(threading.Thread):
    def __init__(self, name, target_thread=None):
        super().__init__(name=name)
        self.target_thread = target_thread
        self.started_event = threading.Event()
        
    def run(self):
        print(f"[{self.name}] 开始执行")
        self.started_event.set()  # 通知主线程已启动
        
        # 模拟一些工作
        time.sleep(1)
        
        print(f"[{self.name}] 尝试join线程: {self.target_thread.name}")
        
        # 关键点：尝试join另一个线程
        if self.target_thread:
            self.target_thread.join()  # 设置超时以便观察
            
        print(f"[{self.name}] 成功完成")

# 创建线程A和线程B
print("===== 创建线程 =====")
thread_a = DeadlockThread("Thread-A")
thread_b = DeadlockThread("Thread-B", target_thread=thread_a)

# 设置互相引用 - 核心死锁点！
thread_a.target_thread = thread_b

print("===== 启动线程 =====")
thread_b.start()  # 注意：先启动B
thread_a.start()

# 等待两个线程都启动
thread_a.started_event.wait()
thread_b.started_event.wait()

print("\n===== 线程状态监控 =====")
print("等待5秒观察线程行为...")
for i in range(10):
    time.sleep(1)
    print(f"[主线程] {i+1}秒: Thread-A状态={thread_a.is_alive()}, Thread-B状态={thread_b.is_alive()}")

print("\n===== 死锁分析 =====")
if thread_a.is_alive() and thread_b.is_alive():
    print("⚠️ 检测到死锁！两个线程都在等待对方结束")
    print("原因: Thread-A 在等待 Thread-B 结束，同时 Thread-B 在等待 Thread-A 结束")
else:
    print("线程成功完成（这通常不会发生）")

print("\n===== 尝试中断死锁 =====")
print("发送键盘中断 Ctrl+C 退出程序")
try:
    while thread_a.is_alive() or thread_b.is_alive():
        time.sleep(1)
except KeyboardInterrupt:
    print("\n强制终止程序")
    sys.exit(1)