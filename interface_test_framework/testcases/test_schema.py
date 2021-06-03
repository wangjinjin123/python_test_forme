"""
sschema校验
https://jsonschema.net/
生成schema文件
根据需要添加自定义规则

场景：需要校验的数据较多时，生成schema


"""
import json

import pytest
import requests
from jsonpath import jsonpath
from jsonschema import validate

def test_get_login_jsonshcema(self):
    url = "https://testerhome.com/api/v3/topics.json"
    data = requests.get(url, params={'limit': '2'}).json()
    schema = json.load(open("topic_schema.json"))
    validate(data, schema=schema)


def test_hogwarts_json():
    r = requests.get('https://ceshiren.com/categories.json')
    #print(r.text)
    assert r.status_code == 200

    pytest.assume(r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号')

    print(jsonpath(r.json(),'$..name'))

    pytest.assume(jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号')
    # assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
    # assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'



