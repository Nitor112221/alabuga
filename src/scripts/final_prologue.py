def prolog(main_hero):
    input()  # необходим холостой клик
    i = 0  # индекс сообщения
    scenario = [  # события в сценарии
        lambda: input("После этой битвы, вас связала королевская стража"),
        lambda: input("Авторитет гоблинов был подавлен"),
        lambda: input("Эльфы по всей провинции поняли, что они могут боротся за свои права также"),
        lambda: input("Как они делали это ещё до войны"),
        lambda: input("Хотя наш герой и пал в темнице"),
        lambda: input("Но его идеи продолжают жить среди эльфов"),
        lambda: input("Конец"),
        lambda: [input(f"Ваша статистика по персонажу:\n{str(main_hero)}")],
    ]
    while True:

        if i == len(scenario):
            break
        scenario[i]()
        i += 1
