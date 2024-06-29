class Armor:
    def __init__(self, protection, name, description):
        self.protection = protection
        self.name = name
        self.description = description

    def get_protection(self):
        return self.protection

    def __str__(self):
        return (f"Название: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Защита: {self.get_protection()}")

    def use(self, owner):
        owner.switch_armor(self)
