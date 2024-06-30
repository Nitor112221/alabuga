from src.entity.Enemy import Enemy
from src.items import weapon, food


def camp_of_thieves(main_hero):
    in_inventory = False
    scenario = [lambda: print("Вы наткнулись на лагерь воров"),
                lambda: print("Вас хотят ограбить"),
                lambda: print("Перед вами 2 человека с ножами"),
                lambda: print("Готовьтесь защищатся"),]
    input()
    scenario[0]()
    input()
    scenario[1]()
    input()
    scenario[2]()
    input()
    scenario[3]()
    enemy = Enemy(40, 4, 1, "Воры")
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
    main_hero.location = 4
    print("Вы победили и получили 400 опыта")
    main_hero.lvl_up(400)
    input()
    print("Общарившись в их лагере, вы украли меч и немного еды")
    input()
    main_hero.get_item(weapon.sword)
    main_hero.get_item(food.apple)
    main_hero.get_item(food.apple)
    main_hero.get_item(food.apple)
    main_hero.get_item(food.steak)
    main_hero.get_item(food.steak)
    print("Получены предметы: Меч, стейк x2, яблоко x3")
    input()
    return True
