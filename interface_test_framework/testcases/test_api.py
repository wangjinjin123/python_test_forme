from interface_test_framework.testcases import test_mulevn


class TestApi:
    data = {
        "method": "get",
        "url": "http://famliy.quickan.com:10000/demo64.txt",
        "headers": None
    }
    def test_send(self):
        res = test_mulevn.Api()
        r = res.send(self.data)
        print(r.text)
