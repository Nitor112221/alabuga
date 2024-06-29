def walk(mainhero):
    in_inventory = False
    i = 0  # индекс сообщения
    scenario = ["Я вышел погулять",
                "Иду",
                "Всё ещё иду",
                "И опять иду"]
    while True:
        command = input()
        if command == 'e':
            in_inventory = True
            print(mainhero)
            print("Чтобы использовать предмет из инвентаря введите его номер")
            print("Чтобы вернутся к игре введите back")
        elif command == "back":
            in_inventory = False
        elif in_inventory and command.isdigit():
            if 0 >= int(command) or int(command) > len(mainhero.inventory):
                print("Неверное число")
                print(mainhero)
                print("Чтобы использовать предмет из инвентаря введите его номер")
                print("Чтобы вернутся к игре введите back")
                continue
            mainhero.use(int(command) - 1)
            print(mainhero)
            print("Чтобы использовать предмет из инвентаря введите его номер")
            print("Чтобы вернутся к игре введите back")

        if not in_inventory:
            print(scenario[i])
            i += 1
