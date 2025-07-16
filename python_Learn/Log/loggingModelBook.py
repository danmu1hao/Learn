# Python 日志系统常用用法笔记
# Python ログシステムのよく使う使い方メモ

# 1. 日志等级（Level）
# 1. ログレベル
#   DEBUG    - 调试信息，最低级别
#              デバッグ情報、一番低いレベル
#   INFO     - 一般运行信息
#              通常の実行情報
#   WARNING  - 警告信息，程序还能继续运行
#              警告情報、プログラムは継続可能
#   ERROR    - 错误信息，程序部分功能受影响
#              エラー情報、一部機能に影響
#   CRITICAL - 严重错误，程序可能无法继续运行
#              重大なエラー、プログラムが継続不可の可能性

# 2. 获取 logger 对象
# 2. logger オブジェクトの取得
import logging
logger = logging.getLogger(__name__)

# 3. Handler（处理器）
# 3. Handler（ハンドラ）
#   - StreamHandler：输出到控制台
#                     コンソール出力
#   - FileHandler：输出到文件
#                   ファイル出力
#   - RotatingFileHandler：自动轮转日志文件
#                           ログファイルの自動ローテーション

# 4. Formatter（格式化器）
# 4. Formatter（フォーマッタ）
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

# 5. 常用方法
# 5. よく使うメソッド
#   logger.debug('调试信息')
#   logger.info('一般信息')
#   logger.warning('警告信息')
#   logger.error('错误信息')
#   logger.critical('严重错误')
#   logger.exception('异常信息（自动带traceback）')
#   logger.log(level, '自定义级别日志')

# 6. 基本配置
# 6. 基本設定
logging.basicConfig(
    level=logging.INFO,  # 设置日志等级
    # ログレベルの設定
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename='example.log',
    filemode='a',
    encoding='utf-8'
)

# 7. 进阶用法：多 Handler、多级别、多格式
# 7. 応用：複数ハンドラ・複数レベル・複数フォーマット
file_handler = logging.FileHandler('multi.log', encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 8. 日志用法示例
# 8. ログの使い方例
logger.debug('调试信息')
logger.info('一般信息')
logger.warning('警告信息')
logger.error('错误信息')
logger.critical('严重错误')
try:
    1 / 0
except Exception as e:
    logger.exception('捕获到异常')
