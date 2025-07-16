# a.py ─ 顶层程序
import logging
import b          # 导入并调用 B
import sys

class CustomFormatter(logging.Formatter):
    def format(self, record):
        s = super().format(record)
        if record.levelno >= logging.ERROR:
            s += '\n'  # error后多一个空行
        return s

file_handler = logging.FileHandler(__file__ + 'error.log', encoding='utf-8', mode='a')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(CustomFormatter('%(asctime)s [%(levelname)s] %(message)s'))

logging.getLogger().addHandler(file_handler)
logging.getLogger().setLevel(logging.ERROR)

def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    # exc_value 就相当于 except 里的 e
    logging.error(f"{exc_type.__name__}: {exc_value}", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = global_exception_handler

def main():
    logging.info("A start")
    b.do_job()
    logging.info("A end")

if __name__ == "__main__":
    b.do_job()
    main()
