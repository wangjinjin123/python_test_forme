import requests

class BecomeMaster:
  @staticmethod
  def become_master(cookie):

      url = "https://distribution.quickcan.cn/distribution/master/become"

      payload={}
      headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'x-device': 'A:dcada7cee7c89a61'
      }

      response = requests.request("POST", url, headers=headers, data=payload)

      print(response.text)
      return response.json()
