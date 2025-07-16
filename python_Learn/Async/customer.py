import asyncio
import random

from python_Learn.Async import service_center


# 用户协程，模拟用户发送请求
# ユーザーコルーチン、リクエスト送信をシミュレート
async def customer(customer_id, service_center):
    await asyncio.sleep(random.uniform(0.1, 1.0))  # 随机等待一段时间后发起请求
    # ランダムな時間待ってからリクエストを送信
    await service_center.handle_request(customer_id)

# 用户只需要知道向客服中心打电话就行,然后等待回应
def CallCenter(customer_id):
    async(service_center.ServiceCenter.handle_request(customer_id))

def generateCustom:
    while(true):

        tasks.append(asyncio.create_task(customer(customer_id, service_center)))
        customer_id += 1
        await asyncio.sleep(random.uniform(0.2, 0.4))  # 随机间隔产生新用户
        # ランダムな間隔で新しいユーザーを生成