import random

# 生成一个 10000~60000 之间的随机端口
# 10000~60000 の間でランダムなポート番号を生成します

def get_random_port():
    # 端口范围
    # ポート範囲
    min_port = 10000
    max_port = 60000
    # 生成随机端口
    # ランダムなポートを生成
    return random.randint(min_port, max_port)

if __name__ == '__main__':
    port = get_random_port()
    print(f"生成的随机端口: {port}")
    print(f"生成したランダムポート: {port}")
