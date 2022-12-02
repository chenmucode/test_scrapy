import requests
#
# response = requests.get(url="http://httpbin.org/ip")
# print(response.text)

# data = {"name":"imooc","key2":"value2"}
# response = requests.get("http://httpbin.org/get",params=data)
# print(response.url)

# response = requests.get("https://www.imooc.com/static/img/index/logo.png")
# with open("imooc.png","wb") as f:
#     f.write(response.content)
# print(response.text)
cookies = dict(cookie_name="imooc")
header={}
response = requests.get(url="http://www.github.com",
                        headers=header,
                        cookies=cookies,
                        timeout=0.001)
data = response.cookies
print(data)
