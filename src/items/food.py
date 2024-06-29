class Food:
    def __init__(self, amount_heal, name, description):
        self.amount_heal = amount_heal
        self.name = name
        self.description = description

    def get_amount_heal(self):
        return self.amount_heal

    def __str__(self):
        return (f"Название: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Исцеляет {self.get_amount_heal()} хп")

    def use(self, owner):
        owner.heal(self.get_amount_heal())


apple = Food(5, "Яблоко", "Вскусное, сочное, сладкое")
steak = Food(15, "Стейк", "Не забываемый вкус мяса")