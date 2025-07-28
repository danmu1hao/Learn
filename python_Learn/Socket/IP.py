HOST = 'localhost'      # 本机，等同于 127.0.0.1
HOST = '127.0.0.1'     # IPv4 本地回环地址
HOST = '::1'           # IPv6 本地回环地址
HOST = '0.0.0.0'      # 监听所有 IPv4 网络接口
HOST = '::'            # 监听所有 IPv6 网络接口

HOST = 'eth0'          # Linux 网络接口名
HOST = 'Wi-Fi'         # Windows 网络接口名
HOST = 'en0'           # macOS 网络接口名

HOST = 'example.com'   # 域名（需要 DNS 解析）
HOST = 'api.github.com' # 远程服务器域名