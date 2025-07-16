"""
log_config.py
全局日志初始化模块：在项目任何地方 `import log_config` 即可。
"""
import logging
import logging.handlers
import os, sys, queue

# ---- 路径与文件 ----
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_PATH = os.path.join(LOG_DIR, "app.log")

# ---- 格式器 ----
FMT = "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s"
formatter = logging.Formatter(FMT, datefmt="%Y-%m-%d %H:%M:%S")

# ---- FileHandler（按天轮转）----
file_hdl = logging.handlers.TimedRotatingFileHandler(
    LOG_PATH, when="midnight", backupCount=10, encoding="utf-8"
)
file_hdl.setFormatter(formatter)
file_hdl.setLevel(logging.INFO)          # 文件收 INFO+

# ---- Console Handler ----
console_hdl = logging.StreamHandler(sys.stdout)
console_hdl.setFormatter(formatter)
console_hdl.setLevel(logging.DEBUG)      # 终端收 DEBUG+

# # ---- 根 logger 装配 ----
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(file_hdl)
root.addHandler(console_hdl)

# ---- 全局异常钩子 ----
def _excepthook(exc_type, exc, tb):
    if issubclass(exc_type, KeyboardInterrupt):
        return sys.__excepthook__(exc_type, exc, tb)
    root.critical("UNCAUGHT EXCEPTION", exc_info=(exc_type, exc, tb))

sys.excepthook = _excepthook
