import asyncio
from bleak import BleakClient
from Crypto.Cipher import AES
from Crypto.Hash import CMAC


# --- 設定 / 配置 ---
SESAME5_MAC = "DF:FD:0D:D3:43:8D"      # 🔹スマートロック実機の MAC（ランダムアドレス）
HANDLE_CCCD = 0x0010                   # 通知有効化に書き込むハンドル
HANDLE_RX   = 0x000e                   # 通知を受け取るハンドル
PRIVATE_KEY_HEX = "daf80ccf3864885736250cd73849354c"  # プライベートキー

Token=0

class RandomCodeReceiver:
    #　初期化
    def __init__(self):
        self.random_code = None
        self.token = None
        self._ev = asyncio.Event()
    #　token生成
    def generate_token(self, private_key_hex):
        if not self.random_code:
            raise ValueError("ランダムコードがまだ受信されていません")
        # プライベートキー（16進文字列）をバイト列に変換
        private_key = bytes.fromhex(private_key_hex)
        # CMACアルゴリズムでTokenを生成
        cobj = CMAC.new(private_key, ciphermod=AES)
        cobj.update(self.random_code)
        self.token = cobj.digest()
        print(f"🔑 Generated Token: {self.token.hex()}")
        global Token  # グローバル変数を宣言
        Token = self.token  # グローバルTokenに代入


    def callback(self, handle: int, data: bytearray):
        print("回収データ")
        print(data)
        # Sesame5 の通知フォーマット：data[0]=ヘッダー, data[1:]=ペイロード
        hdr = data[0]
        if hdr & 0x01:                  # start
            self._buf = bytearray()
        self._buf.extend(data[1:])
        if (hdr >> 1) != 0:             # final
            if len(self._buf) >= 6 and self._buf[0] == 0x08 and self._buf[1] == 0x0e:
                self.random_code = self._buf[2:6]
                print(f"📥 RandomCode: {self.random_code.hex()}")
                # Token生成を試す
                try:
                    self.generate_token(PRIVATE_KEY_HEX)
                    print(Token)
                except Exception as e:
                    print(f"❌ Token生成失败: {e}")
                self._ev.set()

    async def wait_random(self, timeout=5):
        try:
            await asyncio.wait_for(self._ev.wait(), timeout)
            return True
        except asyncio.TimeoutError:
            return False

async def generateToken():
    """Sesame5 からトークンを取得して返す"""
    rc = RandomCodeReceiver()
    print("🔄 Sesame5 に接続中...")
    async with BleakClient(SESAME5_MAC, address_type="random") as cli:
        print("✅ 接続成功")

        # ① Notify 有効化
        await cli.write_gatt_descriptor(HANDLE_CCCD, b"\x01\x00")
        print("🔔 Notify 有効化 OK")

        # ② 通知コールバック登録
        await cli.start_notify(HANDLE_RX, rc.callback)
        print("⏳ RandomCode を待機中…")

        # ③ 受信待ち
        success = await rc.wait_random(timeout=5)
        if not success:
            raise TimeoutError("❌ タイムアウト：RandomCode が届きませんでした。")
        command = bytes([0x02, Token[0], Token[1], Token[2], Token[3]])
        print("➡️ 发送 LoginData:", command.hex(), " ", str(command))
        await cli.write_gatt_char(HANDLE_RX, command, response=False)

        # 4. 応答を待つ（通知コールバックで処理、または直接 read_gatt_char を使用）
        #    サービスが通知を送らない場合は read_gatt_char に切り替える：
        try:
            data = await asyncio.wait_for(cli.read_gatt_char(HANDLE_RX), timeout=15)
            print("📥 Read (direct):", data.hex())
        except asyncio.TimeoutError:
            print("⏱️ 読み取りタイムアウト、直接応答が受信できませんでした")


        
        



asyncio.run(generateToken())
