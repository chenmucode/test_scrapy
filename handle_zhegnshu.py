# 证书校验
import requests

url = "https://requestb.in"
# 通过verfy关键字关闭了ssl证书验证
response = requests.get(url=url,verify=False)
print(response.text)