# Python 包导入与 VS Code 运行说明 / VS Code でのパッケージ読込メモ

> **中日双语：左侧中文解释，右侧日语补充**\
> **中国語がメインで、日本語でポイント補足しています。**

---

## 0 场景 / シナリオ

- 在 **VS Code** 中点击 **Run Code / Run Python File** 或 `F5` 调试时，解释器把 **当前文件夹** 设为工作目录 (`cwd`)。
- 同级或上级包往往 `import` 失败 → `ModuleNotFoundError`。

*VS Code でスクリプトを実行すると「現在のフォルダ」がカレントディレクトリになり、上位パッケージが見えず **`ModuleNotFoundError`** が発生しやすい。*

---

## 1 问题与原因 / 問題と原因

| 现象 (症状)                                        | 根本原因                                | 日本語メモ                             |
| ---------------------------------------------- | ----------------------------------- | --------------------------------- |
| `from moduel import example` 报错                | 运行目录在 `moduel/folder2`，解释器搜索不到父包    | 実行ディレクトリが子フォルダ → 親 `moduel` を探索不可 |
| `python -m moduel.folder2.b` 在 `moduel/` 目录里报错 | `-m` 需要 **包的上一级** 作运行目录；当前目录被当脚本文件夹 | `-m` は 1 階層上で実行しないとパッケージ認識されない    |

---

## 2 四种解决方案 / 4 つの解決策

| #                                                             | 方法         | 关键操作                                                                     | 典型场景      | 日本語要点                |
| ------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------ | --------- | -------------------- |
| **①**                                                         | **动态改 **`` | \`\`\`python                                                             |           |                      |
| import sys, os                                                |            |                                                                          |           |                      |
| PROJECT\_ROOT = os.path.abspath(os.path.join(**file**, '..')) |            |                                                                          |           |                      |
| sys.path.insert(0, PROJECT\_ROOT)                             |            |                                                                          |           |                      |
| \`\`\`                                                        | 单脚本快速运行    | `sys.path` に親ディレクトリ追加                                                    |           |                      |
| **②**                                                         | **命令行 **`` | 在父目录执行：`python -m moduel.folder2.b`                                      | CI / 手动运行 | 親階層から `python -m` 実行 |
| **③**                                                         | ``         | VS Code 调试：指定`"module": "moduel.folder2.b"``"cwd": "${workspaceFolder}"` | 图形调试      | VS Code デバッグ構成       |
| **④**                                                         | ``         | 定义任务：`"command": "python"``"args": ["-m","moduel..."]`                   | 一键运行      | タスクでワンキー実行           |

---

### 方案 ③ & ④ 示例

```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug moduel.folder2.b",
      "type": "python",
      "request": "launch",
      "module": "moduel.folder2.b",
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

```jsonc
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run 指定 Python 模块",
      "type": "shell",
      "command": "python",
      "args": ["-m", "moduel.ModuelImportGuild.taskjsontest"],
      "options": { "cwd": "${workspaceFolder}" },
      "group": { "kind": "build", "isDefault": true },
      "presentation": { "reveal": "always" }
    }
  ]
}
```

---

## 3 参考代码模板 / サンプルコード

```python
"""folder2/b.py"""
import os, sys
PROJECT_ROOT = os.path.abspath(os.path.join(__file__, '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from moduel import example

def test():
    print("this is for test")

test()
```

---

## 4 术语速查 / 用語一覧

| 中文     | 日本語           | English                   |
| ------ | ------------- | ------------------------- |
| 相对路径   | 相対パス          | Relative Path             |
| 绝对路径   | 絶対パス          | Absolute Path             |
| 当前工作目录 | カレントディレクトリ    | Current Working Directory |
| 包 / 模块 | パッケージ / モジュール | Package / Module          |
| 模块搜索路径 | モジュール探索パス     | `sys.path`                |
| 调试配置文件 | デバッグ設定ファイル    | `launch.json`             |
| 任务配置文件 | タスク設定ファイル     | `tasks.json`              |

---

## 总结 / まとめ

> 掌握以上四种方案，可灵活解决 VS Code 下 Python 包导入的常见报错，提升调试与自动化效率。
>
> 上記 4 つの方法を覚えれば、VS Code でのパッケージインポート問題を柔軟に解決できます。

