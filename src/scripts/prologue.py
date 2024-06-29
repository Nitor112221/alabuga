def prolog():
    in_inventory = False
    input()  # необходим холостой клик
    i = 0  # индекс сообщения
    scenario = [  # события в сценарии
        lambda: input("Давным-давно"),
        lambda: input("Эльфы и Гоблины правили Землёй"),
        lambda: input("Но в тот злосчастный день"),
        lambda: input("Война разгорелась со страшной силой"),
        lambda: input("В конце концов Гоблинам удалось победить"),
        lambda: input("Они остались править поверхностью"),
        lambda: input("Но Эльфы не смогли смириться с поражением"),
        lambda: input("Спустя длительное время"),
        lambda: input("1 эльф захотел вернуть величие своей расы на Земле"),
        lambda: input("И освободить свой народ"),
        lambda: input("Этим эльфом стали ВЫ")
    ]
    while True:

        if i == len(scenario):
            break
        scenario[i]()
        i += 1