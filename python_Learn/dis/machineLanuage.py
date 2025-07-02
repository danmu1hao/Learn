import dis
# ---------- ★ カスタム表示関数 / 自定义打印函数 ★ ----------
def pretty_dis(func):
    """関数のバイトコードを表形式で表示 / 以表格方式显示字节码"""
    header = f"{'行(行番号)':<6}{'offset':<8}{'命令(opname)':<20}{'引数(argrepr)'}"
    print(header)
    print("-" * len(header))
    for ins in dis.get_instructions(func):
        # 行番号が無い行は空欄 / 没有源代码行号用空
        line = ins.starts_line if ins.starts_line is not None else ""
        print(f"{str(line):<6}{ins.offset:<8}{ins.opname:<20}{ins.argrepr}")
# ---------- ★ テスト対象 / 测试对象 ★ ----------
def test():
    a = 1
    del a
# ---------- 実行 / 运行 ----------
pretty_dis(test)
