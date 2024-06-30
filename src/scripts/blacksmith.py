from src.items import weapon, armor


def choice(main_hero):
    print("Рассказать свой план? Да/Нет")
    while True:
        answer = input()
        if answer.lower() == "да":
            input("Вы решили поведать кузнецу о своих планах")
            input("[Кузнец] Ого")
            input("[Кузнец] Желаю удачи")
            input("[Кузнец] И в подарок, для такого дела, дам тебе одну из своих последних работ")
            main_hero.get_item(armor.chain_mail)
            input("Вы получили кольчугу")
            break
        elif answer.lower() == "нет":
            input("Вы рассказали ему о жизни, а затем по-дружески побеседовали")
            break
        print("Ответ не распознан, напишите Да или Нет")


def blacksmith(main_hero):
    in_inventory = False
    i = 0  # индекс сообщения
    scenario = [lambda: print("По пути к его дому вы заскачили к знакомому кузницу"),
                lambda: print("[Кузнец] Ах давно не виделись"),
                lambda: print("[Кузнец] Какими судьбами ты к нам?"),
                lambda: choice(main_hero),
                lambda: print("Вы попращались с кузнецом и пошли дальше"),
                lambda: print("Было приятно увидеть старого товарища"),
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
                main_hero.location = 3
                break
            scenario[i]()
            i += 1
