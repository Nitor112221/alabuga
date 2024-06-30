from src.entity.Enemy import Enemy
from src.items import weapon, food


def final_fight(main_hero):
    in_inventory = False
    scenario = [lambda: print("Вы пришли"),
                lambda: print("Дверь перед вами отпирает тот самый Гоблин"),
                lambda: print("[Гоблин] Я знал, что кто-то сюда когда-нибудь придёт"),
                lambda: print("[Гоблин] Сегодня прекрасный денёк"),
                lambda: print("[Гоблин] Птички поют"),
                lambda: print("[Гоблин] Цветочки благаухают"),
                lambda: print("[Гоблин] В такие дни, Эльфы как ты"),
                lambda: print("[Гоблин] В АДУ ГОРЕТЬ ДОЛЖНЫ!!!"),
                lambda: print("[Гоблин] Вот и настал твой конец"),
                lambda: print("[Гоблин] Безумно время проведём, лишь ты и я"),
                lambda: print("[Гоблин] Мы с тобой ведь на правила плевали"),
                lambda: print("[Гоблин] Так давай начнём эту битву и положим возмущениям конец"),
                lambda: print("[Гоблин] Может так эльфы наконец перестанут возмущаться и будут работать молча"),
                ]
    for i in range(len(scenario)):
        input()
        scenario[i]()
    enemy = Enemy(100, 10, 10, "Гоблин царь")
    move = 0  # 0 - ход игрока, 1 - ход врага

    while not enemy.is_dead():
        print(f"Ваш ход, у {enemy.name} осталось {round(enemy.hp, 3)}, у вас {round(main_hero.hp, 3)}")
        command = input()
        if command == 'e':
            in_inventory = True
            print(main_hero)
            print("Чтобы использовать предмет из инвентаря введите его номер")
            print("Чтобы вернутся к игре введите back")
        elif command == "back":
            in_inventory = False
        elif command == "i":
            print(enemy)
        elif command == "a":
            main_hero.hit(enemy)
            move = 1
        elif in_inventory and command.isdigit():
            if 0 >= int(command) or int(command) > len(main_hero.inventory):
                print("Неверное число")
                print(main_hero)
                print("Чтобы использовать предмет из инвентаря введите его номер")
                print("Чтобы вернутся к игре введите back")
                continue
            main_hero.use(int(command) - 1)
            print("Вы использовали предмет")
            move = 1

        if move == 1:
            enemy.hit(main_hero)
        if main_hero.is_dead():
            print("Вы погибли")
            return False
    main_hero.location = 5
    print("Вы победили и получили 10000 опыта")
    main_hero.lvl_up(10000)
    input()

    return True
