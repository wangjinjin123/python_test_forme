#封装mysql类

from sqlalchemy.dialects.mysql import pymysql

from interface_test_combat.common.config import cf
from interface_test_combat.common.get_log import log


class Mysql:
    """
    操作mysql的类
    """
    def __init__(self):
        """
        初始化mysql的conn对象，连接数据库
        """
        #通过配置文件获取数据库的host。port，username，password，charset，database
        host = cf.get_key("mysql","host")
        # 从配置文件获取的值是str，需要转化成int
        port = int(cf.get_key("mysql","port"))
        user = cf.get_key("mysql", "user")
        password = cf.get_key("mysql", "password")
        charset = cf.get_key("mysql", "charset")
        database = cf.get_key("mysql", "database")
        try:
            #连接数据库
            self.conn = pymysql.connect(host=host,port=port,user=user,password=password,charset=charset,database=database)

        except Exception as e:
            log.error(f"无法登陆数据库，错误原因：{e}")

    def select(self, query):
        """
        运行mysql的select语句
        :param query: select语句
        :return: select_data:返回全部的select语句的数据
        """
        log.info(f"selct语句为{query}")
        try:
            #定义游标，并通过excute执行sql语句
            """
            cursor（）：使用当前连接创建并返回游标
            rollback（）：回滚当前事务
            close（）：关闭当前连接
            execute    执行数据库查询或命令，将结果从数据库获取到客户端
            fetchone()：获取结果集的下一行
            fetchmany()：获取结果集的下几行
            fetchall()：获取结果集中剩下的所有行
            rowcount：最近一次的execute返回数据的行数或受影响的行数
            """
            cur = self.conn.cursor()
            cur.excute(query)
            #fetchall读取游标中的所有select数据
            select_data = cur.fetchall()
            log.info("数据查询成功")
            #返回select数据
            return select_data
        except Exception as e:
            log.error(f"insert 语句错误，原因是{e}")

    def insert(self,query):
        """
        运行mysql的select语句
        :param query: insert语句
        :return:
        """
        log.info(f"insert语句为：{query}")
        try:
            #定义游标，并通过excute执行sql语句

            cur = self.conn.cursor()
            cur.excute(query)
            #insert执行成功后commit提交数据

            cur.excute("commit")
            log.info("数据插入成功")

        except Exception as e:
            log.error(f"insert 语句错误，原因是{e}")
            #insert失败后rollback回滚数据
            cur.excute("rollback")

    def delete(self, query):
        """
        运行mysql得delete语句
        :param query: delete语句
        :return:
        """
        log.info(f"delete语句为：{query}")
        try:
            #定义游标，并通过execute执行delete语句
            cur = self.conn.cursor()
            cur.excute(query)
            #delete执行成功后commit提交数据
            cur.excute("commit")
            log.info("数据删除成功")
        except Exception as e:
            log.error(f"selete语句失败，原因：{e}")
            #delete失败后rollback回滚数据
            cur.excute("rollback")
#定义对象为单例模式，其他模块可方便使用
sql = Mysql()

if __name__ == "__main__":
    a = Mysql()
    organizer = "abc"
    cal_id = "abc"






