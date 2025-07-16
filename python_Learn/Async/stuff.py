# 事件数据结构，用于存储客服处理事件的信息
# イベントデータ構造体、カスタマーサービス処理イベントの情報を格納


#说起来分配事件以后客服和用户直接对接，然后，过了任意时间事件解决，客服告诉服务中心解决了
#然后可恶过一段时间给反馈，这个事件关闭
class Stuff:
    def __init__(self):

        # 処理時間
    def resolveQuest(self,customer_id):
        process_time = random.uniform(1, 10.0)
        return process_time
