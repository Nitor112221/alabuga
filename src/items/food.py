class Food:
    def __init__(self, amount_heal, name, description):
        self.amount_heal = amount_heal
        self.name = name
        self.description = description

    def get_amount_heal(self):
        return self.amount_heal

    def __str__(self):
        return (f"\tНазвание: {self.name}\n"
                f"\tОписание: {self.description}\n"
                f"\tИсцеляет {self.get_amount_heal()} хп")

    def use(self, owner):
        owner.heal(self.get_amount_heal())
        owner.remove_item(self)


apple = Food(5, "Яблоко", "Вскусное, сочное, сладкое")
steak = Food(15, "Стейк", "Не забываемый вкус мяса")
