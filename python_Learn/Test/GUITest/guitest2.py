import asyncio
from bleak import BleakScanner

async def main():
    print("正在扫描附近的蓝牙设备...")
    devices = await BleakScanner.discover(timeout=5.0)
    for d in devices:
        if "CANDY HOUSE" in (d.metadata.get("manufacturer_data", {}).get(0x055A, b"")).decode(errors="ignore"):
            print(f"🎯 Sesame 设备发现: {d.address} 名称: {d.name}")
        else:
            print(f"蓝牙设备: {d.address} 名称: {d.name}")

asyncio.run(main())
