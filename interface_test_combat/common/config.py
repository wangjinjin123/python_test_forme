import configparser
import os

#封装该文件是为了获取配置文件config.ini中得值
class ConfigIni:
    """
    获取配置文件
    BASE_PATH:获取当前项目的绝对路径
    congfig_file_path:获取当前配置文件的路径，相当于根路径
    """

    #获取当前项目的绝对路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(BASE_PATH)

    #获取当前配置文件得路径，相当于根路径，读取config.ini配置文件
    config_file_path = os.path.join(BASE_PATH, "config.ini")
    print(config_file_path)


    def __init__(self, file_path=config_file_path):
        '''
        定义一个配置文件的对象，默认一个文件路径，可自己补充其他路径
        :param file_path:配置文件的绝对路径
        '''
        #为了让写入文件的路径是唯一值，故如此定义
        self.config_file_path = file_path
        # 定义配置文件对象,此处使用配置文件解析器，详细可查看：https://docs.python.org/zh-cn/3/library/configparser.html
        self.cf = configparser.ConfigParser()

        #读取配置文件
        self.cf.read(file_path)

    #封装get_key方法获取配置文件中俄value值
    def get_key(self,section,option):
        """
        获取配置文件得value值
        :param section:配置文件中的section的值
        :param option: 配置文件中option的值
        :return value: 返回value的值
        """
        #使用cf对象的get方法获取value值
        value = self.cf.get(section,option)
        return value
    #封装set_value方法修改配置文件中的value值
    def set_value(self,section,option,value):
        """
        修改value的值
        :param section: 配置文件中的section的值
        :param option: 配置文件中option的值
        :param value: 修改的value的值
        :return: 无
        """

        #python内存先修改值
        self.cf.set(section,option,value)

        # 需要通过文件的方式写入才行，不然实体文件的值不会改变
        with open(self.config_file_path,"w+") as f:
            self.cf.write(f)
cf = ConfigIni()

if __name__ == "__main__":
    print(cf.get_key("test1","name4"))
    print(cf.set_value("test1","name1","wang1"))

