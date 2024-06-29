from Base import Base


class MainHero(Base):
    def __init__(self, weapon, armor, lvl, name, xp):
        self.weapon = weapon
        self.armor = armor
        self.lvl = lvl
        self.name = name
        self.exp_for_lvl_up = 50
        self.xp = xp
        self.inventory = []  # инвентарь хранит разные предметы, это могут быть еда для исцеления, броня и оружее
        super().__init__(20 + (lvl - 1) * 3, weapon.get_damage + (lvl - 1) * 0.5, armor.get_protection + (
                    lvl - 1) * 0.5)  # за каждый уровень добавляет + 3 хп и по 0.5 урона и брони

    def switch_weapon(self, new_weapon):
        self.inventory.remove(new_weapon)
        self.inventory.append(self.weapon)
        self.weapon = new_weapon
        self.damage = new_weapon.get_damage() + (self.lvl - 1) * 0.5

    def switch_armor(self, new_armor):
        self.inventory.remove(new_armor)
        self.inventory.append(self.armor)
        self.armor = new_armor
        self.protection = new_armor.get_protection() + (self.lvl - 1) * 0.5

    def use(self, index):  # индекс предмета в инвенторе
        self.inventory[index].use(self)  # у брони, оружия и еды есть метод use по принципу полиморфизм

    def str_inventory(self):
        return "\t\n".join(self.inventory)

    def __str__(self):
        return (
            f"{self.name}:\n"
            f"•Уровень: {self.lvl}\n"
            f"•Максимальное здоровье: {self.max_hp}\n"
            f"•Текущий уровень здоровья: {self.hp}\n"
            f"•Опыта до нового уровня: {self.exp_for_lvl_up - self.xp}"
            f"•Защита: {self.protection}\n"
            f"•Урон: {self.damage}\n"
            f"•Оружее: {self.weapon}\n"
            f"•Броня: {self.armor}\n"
            f"•Инвентарь:\n"
            f"    {self.str_inventory()}")

    def lvl_up(self, amount_xp):
        self.lvl += (amount_xp + self.xp) // self.exp_for_lvl_up
        self.xp = (amount_xp + self.xp) % self.exp_for_lvl_up
        self.damage = self.weapon.get_damage + (self.lvl - 1) * 0.5
        self.protection = self.armor.get_protection + (self.lvl - 1) * 0.5
        self.max_hp = 20 + (self.lvl - 1) * 3

