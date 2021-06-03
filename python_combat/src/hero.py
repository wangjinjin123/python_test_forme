from typing import List

#装饰器：创建一个方法，传入一个函数 返回另一个函数,对初始函数进行二次包装
from python_combat.src.log import log


def log_decorator(func):
    def wrapper(*args, **kwargs):
        log.debug(f'{log_decorator.__name__} --> {func.__name__}')
        return func(*args, **kwargs)
    return wrapper
class Hero:
    #类变量
    hp = 100
    power = 10
    magic_hp = 200
    speed = 1
    tools = []

    def fight(self, hero: 'Hero'):
        while True:
            hero.hp -= self.power
            if self.winner(self, hero):
                return True
            self.hp -= hero.power
            if self.winner(hero, self):
                return False

    #首个参数赢，返回True 反之返回False
    @log_decorator
    def winner(self, hero1, hero2):
        log.debug(f'{hero1} vs {hero2}')
        if hero1.hp <= 0:
            log.debug(False)
            return False
        if hero2.hp <= 0:
            log.debug(True)
            return True



    #打团
    def fight_many(self, heros: List['hero']):
        pass

"""
设计模式：
单例
简单工厂方法
"""








