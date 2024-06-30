from src.items import weapon


def walk(main_hero):
    in_inventory = False
    i = 0  # индекс сообщения
    scenario = [lambda: print("После битвы с манекеном вы поняли, как жестока магия гоблинов"),
                lambda: print("Но вам повезло, разобрав манекен, вы смогли сделать лук"),
                lambda: [main_hero.get_item(weapon.bow), print("Получен новый предмет - Лук")],
                lambda: print("Чтобы взять его в качестве оружия, зайдите в инвентарь, нажав e и enter"),
                lambda: print("Теперь, когда у вас новое оружее, вы можете двигатся дальше"),
                lambda: print("Всю власть в вашем поселении держит лишь 1 гоблин - ваш заклятый враг"),
                lambda: print("Он не помогал развитию города"),
                lambda: print("Как раз таки напротив"),
                lambda: print("Поднимал нологи"),
                lambda: print("Воровал из казны"),
                lambda: print("А также считал всех эльфов своими рабами"),
                lambda: print("Вы решили положить конец его диктатуре")
                ]
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
                main_hero.location = 2
                break
            scenario[i]()
            i += 1
