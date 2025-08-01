import asyncio, time

# 非同期コンテキストマネージャの定義
class AsyncTimer:
    async def __aenter__(self):
        self.t0 = time.perf_counter()
        return self
    async def __aexit__(self, exc_type, exc, tb):
        print(f"{time.perf_counter() - self.t0:.3f}s 経過")

# 非同期関数でasync withを使ってタイマーを計測
async def main():
    async with AsyncTimer():
        await asyncio.sleep(1.5)

asyncio.run(main())
