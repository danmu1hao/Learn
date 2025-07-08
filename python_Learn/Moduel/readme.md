# Python 包导入与 VS Code 运行说明 / VS Code でのパッケージ読込メモ


## 场景 / シナリオ

- 在 **VS Code** 中点击 **Run Code / Run Python File** 或 `F5` 调试时，解释器把 **当前文件夹** 设为工作目录 (`cwd`)。同级或上级包往往 `import` 失败 → `ModuleNotFoundError`。

- *VS Code でスクリプトを実行すると「現在のフォルダ」がカレントディレクトリになり、上位パッケージが見えず **`ModuleNotFoundError`** が発生しやすい。*


---

##  四种解决方案 / 4 つの解決策

---



## 术语速查 / 用語一覧

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



