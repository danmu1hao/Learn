import smtplib
from email.mime.text import MIMEText

mymail = "mymail"
mypass = "mypass"
to_mail = "to_mail"

# メール内容の設定
msg = MIMEText('これはテストメールです。', 'plain', 'utf-8')
msg['Subject'] = 'テストメール'  # 件名
msg['From'] = mymail  # 送信元
msg['To'] = to_mail  # 宛先

# SMTPサーバーに接続してメールを送信
with smtplib.SMTP_SSL('smtpのサーバー', サーバー専用のポート) as server:
    server.login(mymail, mypass)
    server.send_message(msg)

print('メール送信完了')
