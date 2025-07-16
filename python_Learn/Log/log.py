import logging
import time

folder=__file__

# 配置日志，输出到 log.txt 文件
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='log.txt',
    filemode='a',
    encoding='utf-8'   # 指定编码为utf-8
)

count = 0
while True:
    logging.debug(f'第{count}次：这是一个DEBUG日志')
    logging.info(f'第{count}次：这是一个INFO日志')
    logging.warning(f'第{count}次：这是一个WARNING日志')
    logging.error(f'第{count}次：这是一个ERROR日志')
    logging.critical(f'第{count}次：这是一个CRITICAL日志')
    count += 1
    time.sleep(2)  # 每2秒写一次日志
