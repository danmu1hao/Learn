import asyncio
import random
import time

# 方法B：等待随机秒后返回
# メソッドB：ランダムな秒数待ってから返す
async def method_b():
    delay = random.randint(1, 5)
    # 随机等待1~5秒
    # 1〜5秒ランダムに待つ
    await asyncio.sleep(delay)
    return delay

# 方法A：等待方法B，并打印花费的秒数
# メソッドA：メソッドBを待ち、かかった秒数を表示
async def method_a():
    start = time.time()
    seconds = await method_b()
    end = time.time()
    print(f"方法B等待了 {seconds} 秒，A总共花费了 {end - start:.2f} 秒")
    # Bは{seconds}秒待ち、A全体で{end - start:.2f}秒かかりました

# 运行方法A
# メソッドAを実行
if __name__ == "__main__":
    asyncio.run(method_a())
    # asyncio会阻塞主线程再到下一个代码
    print("等待任务完成")
