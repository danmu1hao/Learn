import logging, time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(funcName)s() - %(message)s",
    datefmt="%H:%M:%S"
)

def foo(n):
    return 10 / n   # n==0 时抛异常

for i in range(3, -1, -1):
    try:
        logging.info("开始计算 i=%d", i)
        foo(i)
    except Exception:
        logging.exception("计算出错")
        break
