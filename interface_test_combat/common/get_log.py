import datetime
import logging
import os
import configparser


class Log:

    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    """
    os.path.dirname(path):返回路径 path 的目录名称
    os.path.realpath（file）:返回指定文件的规范路径
    """

    def __init__(self,name="logs"):
        """
        param name: 生成器的名称
        """
        #创建配置文件解析器实例cf
        cf = configparser.ConfigParser()
        self.log_name = name

        #添加日志器
        self.logger = logging.getLogger(name)
        #设置日志级别
        self.logger.setLevel(level=logging.INFO)
        #设置日志格式
        self.f1 = logging.Formatter(fmt='%(asctime)s %(filename)s %(lineno)d %(message)s')
        """
        asctime:当前时间
        filename：日志文件的名称
        lineno：日志的当前行数
        message:日志的信息
        """
        self.f2 = logging.Formatter(fmt='%(asctime)s %(filename)s %(lineno)d >>>>>>> %(message)s')
        #日志文件的名称
        self.filename = 'BASE_PATH'

    #添加一个控制台处理器
    def add_StreamHandler(self):
        #添加控制台处理器
        self.handler = logging.StreamHandler()
        #设置处理器的日志级别
        self.handler.setLevel(level=logging.INFO)
        #给处理器添加（日志输出）格式
        self.handler.setFormatter(self.f1)
        #日志器添加处理器,就拥有了屏幕输出的和文件输出的日志
        self.logger.addHandler(self.handler)

    #添加一个文件处理器
    def add_FileHandler(self):

        #生成日期。创建Log_2020-xx-xx.log文件
        a = self.log_name + "_" + str(datetime.date.today()) + ".log"
        #拼接log文件存放的文件夹和路径
        b = os.path.join(self.BASE_PATH, "logs", a)
        file_mode = self.cf
        #添加文件处理器
        self.filehand = logging.FileHandler()
        #设置处理器的日志级别
        self.filehand.setLevel(level=logging.INFO)
        #处理器添加格式
        self.filehand.setFormatter(self.f2)
        #日志器添加处理器
        self.logger.addHandler(self.filehand)

    def get_log(self):
        """
        运行创建文件处理器和流处理器的代码，最终返回一个logger对象
        :return: logger对象
        """
        #创建了文件处理器
        self.add_StreamHandler()
        #创建流处理器
        self.add_FileHandler()

        #返回记录器，拥有文件和流的处理器和格式，可以输出日志了
        return self.logger

log = Log().get_log()
if __name__ == "__main__":
    log.error("abc")











