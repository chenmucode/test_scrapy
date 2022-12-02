# 使用session省略了cookie的过程
import re
import time
import requests

index_url = "https://account.chinaunix.net/login"
header={}
# 构造一个session
login_session= requests.session()
# 获取登陆页面隐藏div的token，之后用于登陆验证
token_search = re.compile(r'name="_token"\svalue="(.*?)"')
index_response = login_session.get(url=index_url,headers=header)
token_value = re.search(token_search, index_response.text).group(1)
print(token_value)
data = {
    "username":"dazhuang_imooc",
    "password":"abcd1234",
    "_token":token_value,
    "_t": int(time.time())
}
# 登陆
login_url = "http://account.chinaunix.net/login/login"
login_response = login_session.post(url=login_url,headers=header,data=data ) # 使用session请求并保存了cookie
# 最后请求设置页面的url（不用设置cookie）
phone_url ="http://account.chinaunix.net/ucenter/user/index"
phone_response = login_session.get(url=phone_url,headers=header)
print(phone_response.text)