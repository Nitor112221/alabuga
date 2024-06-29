import random

from src.entity.Base import Base


class Enemy(Base):
    def __init__(self, max_hp, damage, protection):
        super().__init__(max_hp, damage, protection)

    def hit(self, hero):
        rand = random.randint(1, 100)
        if rand < 20:
            amount = 0
        elif 20 <= rand <= 70:
            amount = self.damage
        elif 70 < rand <= 85:
            amount = self.damage / 2
        else:
            amount = self.damage * 2
        hero.hurt(amount)
