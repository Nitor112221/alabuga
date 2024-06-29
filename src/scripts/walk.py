def walk(main_hero):
    in_inventory = False
    i = 0  # индекс сообщения
    scenario = [lambda: print("Я вышел погулять"),
                lambda: print("Иду"),
                lambda: print("Всё ещё иду"),
                lambda: print("И опять иду"),
                lambda: [main_hero.hurt(5), print("Вы споткнулись")]]
    while True:
        command = input()
        if command == 'e':
            in_inventory = True
            print(main_hero)
            print("Чтобы использовать предмет из инвентаря введите его номер")
            print("Чтобы вернутся к игре введите back")
        elif command == "back":
            in_inventory = False
        elif in_inventory and command.isdigit():
            if 0 >= int(command) or int(command) > len(main_hero.inventory):
                print("Неверное число")
                print(main_hero)
                print("Чтобы использовать предмет из инвентаря введите его номер")
                print("Чтобы вернутся к игре введите back")
                continue
            main_hero.use(int(command) - 1)
            print(main_hero)
            print("Чтобы использовать предмет из инвентаря введите его номер")
            print("Чтобы вернутся к игре введите back")

        if not in_inventory:
            if i == len(scenario):
                break
            scenario[i]()
            i += 1
