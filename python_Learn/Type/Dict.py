d = {'name': '张三', 'age': 25}
print(d['name'])  # 输出: 张三
print(d.get('age'))  # 比上面那个安全，如果没有key不会报错
print(d.get('weight'))  #输出None
for k, v in d.items():
    print(k, v)