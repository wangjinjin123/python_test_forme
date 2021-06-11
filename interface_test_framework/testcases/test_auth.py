#如何通过auth传递认证信息
import requests
from requests.auth import HTTPBasicAuth


def test_oauth():
    r = requests.get(url= "https://httpbin.testing-studio.com/basic-auth/string/1234",
                 auth = HTTPBasicAuth("string","1234"))
    print(r)
    print(r.text)