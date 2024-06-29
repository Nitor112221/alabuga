class Weapon:
    def __init__(self, damage, name, description):
        self.damage = damage
        self.name = name
        self.description = description

    def get_damage(self):
        return self.damage

    def __str__(self):
        return (f"Название: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Наносит урона: {self.get_damage()}")

    def use(self, owner):
        owner.switch_weapon(self)


stick = Weapon(1, "Палка", "Просто палка, первое что попалось под руку")
sword = Weapon(5, "Меч", "Обычное оружее средневековых людей")
bow = Weapon(4, "Лук", "Дальнобойное оружее. НЕ ОВОЩ")
knife = Weapon(999999999999, "Нож", "Тот самый нож, которым победили Санса")