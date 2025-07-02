# Login.py

import asyncio
import traceback
from bleak import BleakClient
from Crypto.Cipher import AES
from Crypto.Hash import CMAC
from GenerateToken import generateToken  # 名前を合わせる

SESAME5_MAC    = "DF:FD:0D:D3:43:8D"
HANDLE_CCCD    = 0x0010
HANDLE_RX      = 0x000e

# 在文件开头定义
HANDLE_CCCD = 0x0010
HANDLE_RX   = 0x000e  # 通知用句柄
HANDLE_TX   = 0x000c  # 请用实际扫描到的“写特性”句柄




class LoginReceiver:
    def __init__(self):
        self._buf = bytearray()
        self.timestamp = None
        self._ev = asyncio.Event()

    def callback(self, handle: int, data: bytearray):
        # 生データをログ出力
        print(f"[DEBUG] Callback on handle {handle:#04x}, raw data: {data.hex()}")
        hdr = data[0]
        if hdr & 0x01:
            self._buf.clear()
        self._buf.extend(data[1:])

        # 0x02 ヘッダ最終パケットでタイムスタンプ抽出
        if (hdr >> 1) != 0 and len(self._buf) >= 5 and self._buf[0] == 0x02:
            self.timestamp = int.from_bytes(self._buf[1:5], "little")
            print(f"[DEBUG] Parsed timestamp: {self.timestamp}")
            self._ev.set()

    async def wait_login(self, client, cmd: bytes, timeout=5.0) -> int:
        await client.start_notify(HANDLE_RX, self.callback)
        print(f"[DEBUG] Sending login command: {cmd.hex()}")
        await client.write_gatt_char(HANDLE_RX, cmd, False)
        try:
            await asyncio.wait_for(self._ev.wait(), timeout)
            return self.timestamp
        except asyncio.TimeoutError:
            raise TimeoutError("Login response timed out")

async def login() -> int:
    try:
        # ① トークン取得
        token = await generateToken()
        print(f"🔑 Token: {token.hex()}")

        # ② ログインコマンド作成
        cmd = bytes([0x02, token[0], token[1], token[2], token[3]])

        # ③ BLE 接続してログイン
        async with BleakClient(SESAME5_MAC, address_type="random") as cli:
            print("✅ Connected for login")
            await cli.write_gatt_descriptor(HANDLE_CCCD, b"\x01\x00")
            lr = LoginReceiver()
            ts = await lr.wait_login(cli, cmd)
            return ts

    except Exception as e:
        # 詳細なスタックトレースを出力
        print("❌ エラー発生:", str(e))
        traceback.print_exc()
        raise  # 呼び出し側でもわかるよう再送出

if __name__ == "__main__":
    async def main():
        try:
            ts = await login()
            print(f"🎉 Received timestamp: {ts}")

        except Exception:
            # ここでもスタックトレースをキャッチ
            print("❌ メインで例外発生")
            traceback.print_exc()

