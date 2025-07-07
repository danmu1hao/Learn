import requests
from email.mime.text import MIMEText
from email.utils import formatdate
import time
import smtplib
# メールの送り主
from_email = "source@fuga.com"
# メール送信先
to_email = "lsq99199@gmail.com"
# メール件名とメール本文
subject = "メール件名"
message = "メール本文"

def createMIMEText(from_addr, to_addr, message, subject):
    # MIMETextを作成
    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg['Date'] = formatdate()
    return msg

def SendMail():
    createMIMEText(from_email,to_email,message,subject)
    # 连接SMTP服务器并发送
    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login("your_email@example.com", "your_password")
        server.send_message(msg)

# 30分ごとにバッテリーを確認し、条件を満たせばメールを作成
while True:
    # 処理前の時刻
    time1 = time.time()

    # バッテリー確認処理
    try:
        response = requests.get("https://app.candyhouse.co/api/sesame2/11200413-0002-0611-3F00-9200FFFFFFFF")
        # 仮のバッテリー値取得（実際はresponse.json()などで取得）
        # battery_percentage = response.json().get('batteryPercentage', 100)
        battery_percentage = 25  # デモ用の仮値
        if battery_percentage <= 30:
            mime = createMIMEText(from_email, to_email, message, subject)
            print("mime", mime)
    except Exception as e:
        print("バッテリー確認中にエラー:", e)

    # 最後に
    time2 = time.time()
    # これで、でんげんがついている間は常に動く、ただし一度一連の作業を行った場合は30分間は行わない、ということが実現できるはず。
    sleep_time = max(0, 1800 - (time2 - time1))
    time.sleep(sleep_time)