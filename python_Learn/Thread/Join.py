import threading
import time
"""
出力
foo0
foo1
foo2
foo3
foo4
---end---
"""
def threadFoo():
    for i in range(5):
        print("foo" + str(i))
        time.sleep(1)

if __name__ == "__main__":
    thread = threading.Thread(target=threadFoo, name='thread1',daemon=True)
    thread.start()
    
    #ここでthread終わるまで進めない
    print("---end---")
