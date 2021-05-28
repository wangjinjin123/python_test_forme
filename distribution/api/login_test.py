import pytest
import requests


class TestLogin:
    @staticmethod
    def test_login():
        url = "https://api.quickcan.cn/v2/phone/signin"
        payload = 'phone=13728814523&password=11111111w'
        headers = {
            'User-Agent': 'Kuaikan/5.93.1/593100(Android;6.0.1;OPPO R9s;kuaikan17;WIFI;1920*1080)',
            'app-info': 'eyJLS0RJRCI6IkEyMDIwMDMyNzA5Mzk0OTc2MzYzNjEyMjg4Mzg1MDQ2IiwiYWVnaXNfYXBwX2lkIjoiMTAwMDAwMTI0MCIsImFuZHJvaWRfaWQiOiJkY2FkYTdjZWU3Yzg5YTYxIiwiYXBwX3NlY3JldF9zaWduIjoiOTY3NGMxNWY3YmY1ZGRiNGRiZjhiNGVlNjgyMTAyYWIiLCJiZCI6Ik9QUE8iLCJjYSI6MCwiY3QiOjIwLCJkZXZ0IjoxLCJkcGkiOjQ4MCwiZ3BzX3RpbWUiOjAsImhlaWdodCI6MTkyMCwiaW1laSI6Ijg2NDA4MDAzNTgzODU3OSIsImltc2kiOiIiLCJra19jX3QiOjE2MjE4NTE5NjczNDgsImtrX3NfdCI6MTYyMTg1MTk2NTE2MiwibWFjIjoiZTQ6NDc6OTA6Y2Q6OWU6YTMiLCJtb2RlbCI6Ik9QUE8gUjlzIiwib2FpZCI6IiIsIm92IjoiNi4wLjEiLCJwaG9uZU51bWJlciI6IiIsInVzZXJfZ3JvdXAiOiJub3JtYWwiLCJ2aXNpdG9yX3NpZ24iOiJiZGY2NzU5OWFmZWFmYzgzYTdmNTY0ZjdlNTZjNjc3YSIsIndpZHRoIjoxMDgwfQ==',
            'x-device': 'A:dcada7cee7c89a61',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.json())
        print(response.cookies)
        return response


if __name__ == '__main__':
    pytest.main()
