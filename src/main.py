import os

from src.entity.MainHero import MainHero
import src.items.weapon as weapon
import src.items.food as food
import src.items.armor as armor
import src.scripts.walk as walk
import json

from src.scripts import prologue, blacksmith, camp_of_thieves, final_fight, final_prologue
from src.scripts.first_fight import first_fight


def load_data():
    global main_hero
    with open("resource/stats.json", "r", encoding="UTF-8") as file:
        stats = json.load(file)
        items = {
            "Палка": weapon.stick,
            "Меч": weapon.sword,
            "Лук": weapon.bow,
            "Бинт": armor.bandage,
            "Яблоко": food.apple,
            "Стейк": food.steak,
            "Нож": weapon.knife,
            "Кольчуга": armor.chain_mail
        }

        main_hero = MainHero(items[stats["weapon"]], items[stats["armor"]], stats["lvl"], stats["name"],
                             stats["xp"], stats["location"])

        for i in stats["inventory"]:
            main_hero.get_item(items[i])


def save_data():
    global main_hero
    stats = {"name": main_hero.name,
             "lvl": main_hero.lvl,
             "xp": main_hero.location,
             "weapon": main_hero.weapon.name,
             "armor": main_hero.armor.name,
             "inventory": [i.name for i in main_hero.inventory],
             "location": main_hero.location}
    with open("resource/stats.json", "w", encoding="utf-8") as file:
        json.dump(stats, file, indent=4)


main_hero = None


# Гайд
print("УПРАВЛЕНИЕ")
print("чтобы вызвать команду, введите с клавиатуры нужную команду и нажмите enter")
print("КОМАНДЫ")
print("e - открыть инвентарь")
print("back - выйти из инвентаря")
print("Просто enter - продолжить")
print("Чтобы начать нажмите enter")


# загрузка сохранения/создание нового персонажа
if os.path.isfile("resource/stats.json"):
    load_data()
else:
    # если игру запустили в первый раз, то игроку нужно показать пролог
    prologue.prolog()
    name = input("Назовите своего персонажа: ")
    if name == "Chara":  # отсылка
        main_hero = MainHero(weapon.knife, armor.bandage, 1, name, 0, 0)
    else:
        main_hero = MainHero(weapon.stick, armor.bandage, 1, name, 0, 0)
    main_hero.get_item(food.apple)
    main_hero.get_item(food.apple)
    main_hero.get_item(food.apple)
    main_hero.get_item(food.steak)
    save_data()

# запуск истории
while main_hero.location == 0 and not first_fight(main_hero):
    load_data()
save_data()
load_data()  # загрузка нужна, чтобы востановить здоровье после сценария
while main_hero.location == 1:
    walk.walk(main_hero)
    save_data()
    load_data()
while main_hero.location == 2:
    blacksmith.blacksmith(main_hero)
    save_data()
    load_data()
while main_hero.location == 3 and not camp_of_thieves.camp_of_thieves(main_hero):
    load_data()
save_data()
load_data()
while main_hero.location == 4 and not final_fight.final_fight(main_hero):
    load_data()
save_data()
load_data()
final_prologue.prolog(main_hero)
