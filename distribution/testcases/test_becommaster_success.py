import json

import requests
import pytest

from distribution.api.becom_master import BecomeMaster
from distribution.api.login_test import TestLogin


class TestBecomeMaster:
    # def set_up(self):
    #     # s = requests.session()
    #     self.login = Login()
    #     self.becomemaster = BecomeMaster()
    #     # print(s)

    # def test_login1(self):
    #     r1 = TestLogin.test_login()
    #     r1_1=r1.json()
    #     print(type(r1_1))
    #     print(r1_1)
    #     print(r1_1['code'])
    #     print(r1.cookies)
    #     assert (r1_1['code']) == 200

    def test_become_master1(self):
        res = TestLogin.test_login()
        # print(res)
        cookie = res.cookies
        print(cookie)
        r2 =BecomeMaster.become_master(cookie)
        # print(r2)
        assert (r2['success']) == 'true'

if __name__ == '__main__':
    pytest.main()






