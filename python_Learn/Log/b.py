# b.py ─ 子系统
import logging
logger = logging.getLogger("module.b")

def do_job():
    print(1/0)
    logger.info("B job running")
