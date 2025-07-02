# Process.py 例
from multiprocessing import Process, freeze_support
import time, os

def task():
    for _ in range(3):
        print("PID:", os.getpid(), "working")
        time.sleep(1)

# ★ ガードを付ける ★
if __name__ == '__main__':
    freeze_support()          # PyInstaller で exe 化する場合のみ必須
    p = Process(target=task)
    p.start()
    p.join()
    print("Main done")
