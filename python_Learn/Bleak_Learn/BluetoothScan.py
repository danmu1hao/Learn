import asyncio
from bleak import BleakScanner
"""
周囲のデバイスをスキャンするコード
    devices=BleakScanner.discover()
type(devices):
    <class 'list'>
出力サンプル:
    F8:B2:DE:CF:FC:E6: Apple, Inc. (b'\x12\x02.\x01\x07\x11\x06\xfa\x08*\x83\xe8\x1f\x8c\xa97{\xf6\x8b\x1b7.\xc0')
type(device) in devices:
    <class 'bleak.backends.device.BLEDevice'>
なぜ：
    BLEDeviceクラスは__str__()を実装しているため、読みやすい形式（例: F8:B2:DE:CF:FC:E6: Apple, 
    Inc.）で表示されます。
"""
async def run():
    # ★ timeout を秒数で指定（例：15 秒）
    devices = await BleakScanner.discover(timeout=3.0, scanning_mode="active")
    for d in devices:
        print(d)

if __name__ == "__main__":
    # 非同期関数を実行
    asyncio.run(run())
