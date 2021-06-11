
import pytest

from interface_test_combat.api.address_model import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid, mobile",[('wang1','13728814500'),('wang2','13728814501'),('wang3','13728814502')])
    def test_add_user(self,userid,mobile):
        name = "星期四"
        department = [1]
        print(userid)
        print(mobile)
        #数据清理
        self.address.dele_user(userid)
        #创建成员
        r = self.address.add_user(userid,name,mobile,department)
        print(r)
        assert r.get("errcode") == 0
        #查询成员确认创建成功
        r = self.address .get_user(userid)
        #print(r)
        #此处使用python字典的get方法获取字典中的value
        assert r.get("name", "userid 添加失败") == name



