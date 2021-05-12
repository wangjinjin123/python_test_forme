#简单工厂方法
from python_combat.src.chengyaojin import ChengYaoJin
from python_combat.src.hero import Hero
from python_combat.src.libai import LiBai
from python_combat.src.log import log


class HeroFactory:
    @classmethod
    def creat_hero(cls, name:str) -> Hero:
        if name == '程咬金':
            return ChengYaoJin()
        elif name == '李白':
            return LiBai()
        else:
            log.error(f"don't know how to creat hero {name}")
            return None



