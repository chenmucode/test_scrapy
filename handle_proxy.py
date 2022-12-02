import requests

# 代理可以使用阿布云 abuyun.com

# 带用户名和密码的代理。动态版的代理每次请求代理ip都不一样
proxy = {
    "http": "http://name:password@http-dyn.abuyun.com:9020",
    "https": "http://name:password@http-dyn.abuyun.com:9020",
}
url = "http://httpbin.org/ip"

for i in range(5):
    # 设置了代理的关键字proxies
    response = requests.get(url=url, proxies=proxy)
    print(response.text)
