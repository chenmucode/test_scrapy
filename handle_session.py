import re
import requests


class Login(object):
    def __init__(self):
        # 初始化session对象
        self.request_session = requests.session()
        # 定义请求头
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }
        self.csrf_value = ""

    # 获取csrf token值的方法
    def handle_csrf_token(self):
        # 商品列表页url
        self.index_url = "http://flask.zhaedu.com/mall/product/list/1"
        # 发送一个get请求
        csrf_response = self.request_session.get(url=self.index_url, headers=self.header)
        # 通过正则 从返回体中获取csrf_token
        csrf_search = re.compile(r'name="csrf_token"\stype="hidden"\svalue="(.*?)">')
        self.csrf_value = csrf_search.search(csrf_response.text).group(1)

    # 开始登陆
    def handle_login(self):
        self.handle_csrf_token()
        username = "admin"
        password = "123456"
        login_url = "http://flask.zhaedu.com/accounts/login"
        data = {
            "csrf_token": self.csrf_value,
            "username": username,
            "password": password
        }
        # 发送post请求（一定要加上data），保存了cookie
        self.request_session.post(url=login_url, headers=self.header, data=data)
        # 通过session获取商品列表信息
        response = self.request_session.get(url=self.index_url, headers=self.header)
        print(response.text)


if __name__ == '__main__':
    flask_login = Login()
    flask_login.handle_login()
