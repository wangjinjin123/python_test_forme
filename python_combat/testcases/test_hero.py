import unittest
from unittest import TestCase

from python_combat.src.chengyaojin import ChengYaoJin
from python_combat.src.hero_factory import HeroFactory
from python_combat.src.libai import LiBai


class TestHero(TestCase):
    def test_fight(self):
        #第一轮对打
        chengyaojin = ChengYaoJin()
        libai = LiBai()
        #子类可使用父类的类方法
        assert chengyaojin.fight(libai) == True

        #第二轮对打（重新开始打）
        # chengyaojin = ChengYaoJin()
        # libai = LiBai()
        chengyaojin = HeroFactory.creat_hero('程咬金')
        libai = HeroFactory.creat_hero('李白')

        assert libai.fight(chengyaojin) == False

    def test_log(self):
        import logging
        logging.debug('Debugging information')
        logging.info('Informational message')
        logging.warning('Warning:config file %s not found', 'server.conf')
        logging.error('Error occurred')
        logging.critical('Critical error -- shutting down')




if __name__ == '__main__':
    unittest.main()



