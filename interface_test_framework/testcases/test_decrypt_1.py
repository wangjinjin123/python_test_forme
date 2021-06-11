from interface_test_framework.testcases import test_decrypt
import pytest

class TestApiRequest:
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:10000/demo64.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        #实例化
        ar = test_decrypt.ApiRequest()
        print(ar.send(self.req_data))


