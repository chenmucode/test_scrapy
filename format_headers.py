import json
import re

def format(headers):
    map = dict()
    try:
        pattern = re.compile("^(.*?):(.*)$")
        new_str = "{"
        for line in headers.splitlines():
            new_line = re.sub(pattern, "\"\\1\":\"\\2\",", line).rstrip(" ")
            new_str += new_line
        new_str = new_str.rstrip(',') + '}'
        map = json.loads(new_str)
    except Exception as e:
        print(e)
    finally:
        return map


if __name__ == '__main__':
    a = """Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: XSRF-TOKEN=wbYPqOeR3o0VeDUhxw6R234ope5eiBtQ6MDUq1M8; laravel_session=gAxSGpxzRN0XTExls5nqkBGaz74QW8uGGq8tc4F9; account_chinauni=accountchinauni
Host: account.chinaunix.net
Referer: http://account.chinaunix.net/
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest"""
    format(a)