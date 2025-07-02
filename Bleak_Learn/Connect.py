import asyncio
from bleak import BleakClient
SESAME5_MAC = "DF:FD:0D:D3:43:8D"  
HANDLE_CCCD = 0x0010
HANDLE_RX = 0x000e
async def run():
    print("🔄 Sesame5 に接続中...")
    async with BleakClient(SESAME5_MAC, address_type="random") as cli:
        # ① Notify 有効化
        await cli.write_gatt_descriptor(HANDLE_CCCD, b"\x01\x00")
        value = await cli.read_gatt_char(HANDLE_RX)
        print("📥 Read:", value.hex())

if __name__ == "__main__":
    asyncio.run(run())
