from src.entity.Base import Base


class Enemy(Base):
    def __init__(self, max_hp, damage, protection):
        super().__init__(max_hp, damage, protection)

    def hit(self, target):
        pass

