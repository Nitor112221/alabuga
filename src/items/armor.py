class Armor:
    def __init__(self, protection, name, description):
        self.protection = protection
        self.name = name
        self.description = description

    def get_protection(self):
        return self.protection

    def __str__(self):
        return (f"\tНазвание: {self.name}\n"
                f"\tОписание: {self.description}\n"
                f"\tЗащита: {self.get_protection()}")

    def use(self, owner):
        owner.switch_armor(self)


bandage = Armor(2, "Бинт", "Тканевая повязка, не стоит от неё многое ожидать")
chain_mail = Armor(20, "Кольчуга", "Прочная броня, защищающая носителя")