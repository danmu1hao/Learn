import asyncio
from bleak import BleakClient

address = "DF:FD:0D:D3:43:8D"
notify_char = "16860003-a5ae-9856-b6d3-dbb4c676993e"

def handle_notification(sender, data):
    print(f"\n📩 收到通知 from {sender}: {data.hex()}")

async def main():
    async with BleakClient(address) as client:
        print("✅ 已连接")
        await client.start_notify(notify_char, handle_notification)

        print("⏳ 正在监听通知（10秒）...")
        await asyncio.sleep(10)  # 可调整时间
        await client.stop_notify(notify_char)

asyncio.run(main())
