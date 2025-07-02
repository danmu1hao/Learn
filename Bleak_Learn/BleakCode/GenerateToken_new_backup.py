import asyncio
from bleak import BleakClient
from Crypto.Cipher import AES
from Crypto.Hash import CMAC


# --- 設定 / 配置 ---
SESAME5_MAC = "DF:FD:0D:D3:43:8D"      # 🔹スマートロック実機の MAC（ランダムアドレス）
HANDLE_CCCD = 0x0010                   # 通知有効化に書き込むハンドル
HANDLE_RX   = 0x0e                   # 通知を受け取るハンドル、
PRIVATE_KEY_HEX = "daf80ccf3864885736250cd73849354c"  # プライベートキー
has_run = False
Token=0

# token生成
def generate_token(random_code, private_key_hex):
    if not random_code:
        raise ValueError("ランダムコードがまだ受信されていません")

    print(f"📥RandomCode: {random_code.hex()}")
    temp=random_code
    random_code = bytes([
        temp[2],
        temp[3],
        temp[4],
        temp[5]
    ])
    print(f"📥RandomCode: {random_code.hex()}")
    # プライベートキー（16進文字列）をバイト列に変換
    private_key = bytes.fromhex(private_key_hex)
    # CMACアルゴリズムでTokenを生成
    cobj = CMAC.new(private_key, ciphermod=AES)
    cobj.update(random_code)
    token = cobj.digest()
    print(f"🔑 Generated Token: {token.hex()}")
    global Token  # グローバル変数を宣言
    Token = token  # グローバルTokenに代入


class SasemiConnection:
    #　初期化
    def __init__(self):
        self.random_code = None
        self.token = None
        self._ev = asyncio.Event()
        self._buf = bytearray()
        self._encrypt_counter = 0
        self._decrypt_counter = 0
        self._last_item_code = 0
        self._buffer = bytes()
        
    #  コールバック関数 sasemiからメッセージを受信すると自動呼出し
    def callback(self, handle: int, data: bytearray):
        print("受信データ")
        print(data)
        # Sesame5 の通知フォーマット：data[0]=ヘッダー, data[1:]=ペイロード
        hdr = data[0]
        if hdr & 0x01:                  
            self._buf = bytearray()
        self._buf.extend(data[1:])
        if (hdr >> 1) != 0:
            # もし受信したのは登録用randomcodeなら  
            if len(self._buf) >= 6 and self._buf[0] == 0x08 and self._buf[1] == 0x0e:
                # 重複ログインを防止する
                global has_run
                if has_run:
                    return
                else:
                    has_run=True
                self.random_code = bytes(self._buf)
                # token生成を試す
                try:
                    generate_token(self.random_code,PRIVATE_KEY_HEX)
                except Exception as e:
                    print(f"❌ Token生成失败: {e}")
                self._ev.set()
        
        # 通用通知处理
        self.handleNotification(handle, data)

    def handleNotification(self, cHandle, data):
        if (data[0] & 1) != 0:
            self._buffer = bytes()
        self._buffer += data[1:]
        if (data[0] >> 1) == 0:
            return

        if (data[0] >> 1) == 2:
            data = self.decrypt(self._buffer)
        else:
            data = self._buffer

        op_code = data[0]
        self._last_item_code = data[1]
        
        print(f"📥 收到响应: op_code={op_code}, item_code={self._last_item_code}")
        
        # 根据 op_code 和 item_code 处理不同的响应
        if op_code == 0x08 and self._last_item_code == 0x0e:
            # Random code 响应
            print("🔑 收到 Random Code")
        elif op_code == 0x02:
            # Login 响应
            print("🔐 Login 响应")
        elif op_code == 0x53:
            # Unlock 响应
            print("🔓 Unlock 响应")
        else:
            print(f"❓ 未知响应: op_code={op_code}, item_code={self._last_item_code}")

    async def receive(self, cli, item_code):
        """等待特定 item_code 的响应"""
        self._last_item_code = 0
        waiting_count = 0
        
        while self._last_item_code != item_code:
            # 等待通知
            try:
                # 在异步环境中，我们需要使用事件或其他机制来等待通知
                # 这里我们使用一个简单的轮询机制
                await asyncio.sleep(0.1)  # 等待100ms
                waiting_count += 1
                if waiting_count >= 100:  # 10秒超时
                    raise TimeoutError("等待响应超时")
            except Exception as e:
                print(f"❌ 等待响应时出错: {e}")
                raise
        
        print(f"✅ 收到期望的响应: item_code={item_code}")
        return True

    async def wait_random(self, timeout=5):
        try:
            await asyncio.wait_for(self._ev.wait(), timeout)
            return True
        except asyncio.TimeoutError:
            return False

    def send(self, peri, send_data, is_encrypt):
        # 暗号化が必要ならデータを暗号化
        if is_encrypt:
            send_data = self.encrypt(send_data)

        # 送信データの残りバイト数を取得
        remain = len(send_data)
        offset = 0

        # データが残っている限りループ
        while remain > 0:
            header = 0

            # 最初のチャンクなら開始フラグをセット
            if offset == 0:
                header |= 0x01

            # 最後のチャンク判定
            if remain <= 19:
                # 残り全てを取り出し
                buffer = send_data[offset:]
                remain = 0
                # 暗号化ありなら暗号化終了フラグ(0x04)、なしなら通常終了フラグ(0x02)をセット
                header |= 0x04 if is_encrypt else 0x02
            else:
                # 19 バイト分を取り出す
                buffer = send_data[offset:offset+19]
                offset += 19
                remain -= 19

            # ヘッダーバイトとデータを連結してパケット化
            packet = bytes([header]) + buffer

            # 指定ハンドル(0x000d)のキャラクタリスティックに書き込む
            peri.writeCharacteristic(0x000d, packet, False)

    def encrypt(self, data):
        if not self.random_code or not Token:
            raise ValueError("random_code 或 token 未设置")
            
        iv = self._encrypt_counter.to_bytes(9, "little")
        iv += self.random_code
        cobj = AES.new(Token, AES.MODE_CCM, iv, mac_len=4, msg_len=len(data), assoc_len=1)
        self._encrypt_counter += 1
        cobj.update(bytes([0]))
        enc_data, tag = cobj.encrypt_and_digest(data)
        tag4 = tag[0:4]
        return enc_data + tag4

    def decrypt(self, data):
        if not self.random_code or not Token:
            raise ValueError("random_code 或 token 未设置")
            
        iv = self._decrypt_counter.to_bytes(9, "little")
        iv += self.random_code
        cobj = AES.new(Token, AES.MODE_CCM, iv)
        self._decrypt_counter += 1
        decode_data = cobj.decrypt(data[0:-4])
        return decode_data

async def SasemiConect():
    rc = SasemiConnection()
    print("🔄 Sesame5 に接続中...")
    async with BleakClient(SESAME5_MAC, address_type="random") as cli:
        print("✅ 接続成功")

        # ① Notify 有効化
        await cli.write_gatt_descriptor(HANDLE_CCCD, b"\x01\x00")
        print("🔔 Notify 有効化 OK")

        # ② 通知コールバック登録　受信するとcallbackを執行
        await cli.start_notify(HANDLE_RX, rc.callback)
        print("⏳ RandomCode を待機中…")

        # ③ 受信待ち
        success = await rc.wait_random(timeout=5)
        if not success:
            raise TimeoutError("❌ タイムアウト：RandomCode が届きませんでした。")
        
        # ④ ログインコマンド送信
        command = bytes([0x02, Token[0], Token[1], Token[2], Token[3]])
        print("➡️ 発送 LoginData:", command.hex()," ", str(command))
        await cli.write_gatt_char(HANDLE_RX, command, response=False)
        
        # 等待登录响应
        try:
            await rc.receive(cli, 0x02)  # 等待登录响应
            print("✅ 登录成功")
        except TimeoutError:
            print("❌ 登录响应超时")

        # ⑤ 解錠コマンド送信
        tag = '自前プログラムから解錠'.encode()
        command = bytes([0x53, len(tag)]) + tag
        print("➡️ 発送 unlock:", command.hex()," ", str(command))
        await cli.write_gatt_char(HANDLE_RX, command, response=False)
        
        # 等待解锁响应
        try:
            await rc.receive(cli, 0x53)  # 等待解锁响应
            print("✅ 解锁成功")
        except TimeoutError:
            print("❌ 解锁响应超时")

        try:
            data = await asyncio.wait_for(cli.read_gatt_char(HANDLE_RX), timeout=15)
            print("📥 Read (direct):", data.hex())
        except asyncio.TimeoutError:
            print("⏱️ 読み取りタイムアウト、直接応答が受信できませんでした")

if __name__ == "__main__":
    asyncio.run(SasemiConect())