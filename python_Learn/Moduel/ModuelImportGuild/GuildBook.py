# Python 模块加载 & 路径设置实验  
# モジュール読み込みとパス操作の例

import sys  # 系统模块，提供解释器相关接口（如 sys.path）  
# システムモジュール、インタプリタ関連のインターフェース（例：sys.path）を提供

# 你可以看到当前包含的模块搜索路径列表
# 現在含まれているモジュール探索パスのリストを確認できます
print(sys.path)

import os   # 操作文件路径（跨平台路径拼接等）  
# ファイルパス操作（クロスプラットフォームのパス結合など）

# 🔧 添加项目根目录到模块搜索路径中  
# 🔧 プロジェクトのルートディレクトリを sys.path に追加する
Relative_Path = os.path.join(                                 
    os.path.dirname(__file__),                
    # 当前文件所在目录 此外，join连接两个路径的时候会在中间自动加上/  
    # 現在のファイルがあるディレクトリ。さらに、joinで2つのパスを結合すると、間にスラッシュが自動的に入ります。
    '..'                                      
    # 上一级目录 → 项目根目录（例：.../moduel）  
    # 1つ上のディレクトリ → プロジェクトルート（例：.../moduel）
    # 此外，有趣的是，你无法将文件夹命名为.. 这是为了方便电脑认知路径，..统一视作上级文件夹  
    # ちなみに、フォルダ名を「..」にはできません。これはOS側で「..」を常に上の階層と認識するように決められているからです。
)

PROJECT_ROOT = os.path.abspath(
    Relative_Path  # 转为绝对路径  
    # 絶対パスに変換
)

# 如果路径尚未在 sys.path 中，插入最前（优先级最高）  
# まだ追加されていなければ、先頭に挿入（最優先で探索）

# sys.path 当你执行 import xxx 时，去这些目录里找 xxx.py 或 xxx/__init__.py  
# sys.path は import xxx を実行するとき、これらのディレクトリで xxx.py または xxx/init.py を探します

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# 🚧 输出确认添加的路径  
# 🚧 確認用にパスを出力
print(PROJECT_ROOT)

# 📦 从项目根目录导入 example 模块 由于我们已经把moduel添加到识别路径，所以可以认知  
# 📦 プロジェクトルートから example モジュールをインポート。すでに moduel を sys.path に追加したので、認識されます。

import example

# ▶️ 调用 example 模块的 test() 函数  
# ▶️ example モジュール内の test() 関数を呼び出す
example.test()
