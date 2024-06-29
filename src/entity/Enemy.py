import random

from src.entity.Base import Base


class Enemy(Base):
    def __init__(self, max_hp, damage, protection, name):
        super().__init__(max_hp, damage, protection)
        self.name = name

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

    def __str__(self):
        return (f"Враг: {self.name}\n"
                f"Урон: {self.damage}\n"
                f"Защита: {self.protection}\n"
                f"Здоровье: {self.hp}")
