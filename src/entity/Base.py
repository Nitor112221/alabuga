class Base:
    def __init__(self, max_hp, damage, protection):
        self.max_hp = max_hp
        self.damage = damage
        self.protection = protection
        self.hp = max_hp

    def is_dead(self):
        return self.hp <= 0

    def hit(self, target):
        target.hurt(self.damage)

    def hurt(self, amount):
        self.hp -= amount * ((100 - self.protection) / 100)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)


