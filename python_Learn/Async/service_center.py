import asyncio
import random
from stuff import Stuff

# 处理中心，负责接收请求并分配客服
# サービスセンター、リクエストを受け取りカスタマーサービスに割り当てる
class ServiceCenter:
    def __init__(self):
        self.event_log = []  # 事件日志
        # イベントログ

    async def handle_request(self, customer_id):
        # 分配客服处理请求
        # カスタマーサービスにリクエストを割り当て

        await asyncio.sleep(process_time)  # 客服处理时间
        # カスタマーサービスの処理時間

        self.event_log.append(stuff)
        print(f"客服完成了用户{customer_id}，处理时间：{process_time:.2f}秒")
        # カスタマーサービスはユーザー{customer_id}を完了、処理時間：{process_time:.2f}秒

    def show_log(self):
        # 打印所有事件日志
        # すべてのイベントログを表示
        for stuff in self.event_log:
            print(f"用户{stuff.customer_id}，处理时间：{stuff.process_time:.2f}秒")
            # ユーザー{stuff.customer_id}、処理時間：{stuff.process_time:.2f}秒

# 主运行逻辑，持续产生用户请求
# メイン実行ロジック、ユーザーリクエストを継続的に生成

def generateStuff:
    stuffList=list()
    for _ in range(5):
        stuff = Stuff()
        stuffList.insert(stuff)


async def main():
    service_center = ServiceCenter()
    customer_id = 1
    tasks = []

    await asyncio.gather(*tasks)
    print("所有用户请求处理完毕，事件日志如下：")
    # すべてのユーザーリクエストが完了、イベントログ：
    service_center.show_log()




if __name__ == "__main__":
    asyncio.run(main())
