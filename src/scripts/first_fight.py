from src.entity.Enemy import Enemy


def first_fight(main_hero):
    in_inventory = False
    scenario = [lambda: print("Я встретили живого манекена"),
                lambda: print("Живой манекен преграждает дорогу"),
                lambda: print("Вам нужно его сломать"),
                lambda: print("Чтобы бить манекен введите символ a"),
                lambda: print("Чтобы посмотреть информацию о враге введите символ i")]
    input()
    scenario[0]()
    input()
    scenario[1]()
    input()
    scenario[2]()
    input()
    scenario[3]()
    input()
    scenario[4]()
    enemy = Enemy(10, 3, 10, "Манекен")
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
    main_hero.location = 1
    print("Вы победили и полусили 50 опыта")
    main_hero.lvl_up(50)
    return True
