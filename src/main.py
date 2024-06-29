import os

from src.entity.MainHero import MainHero
import src.items.weapon as weapon
import src.items.food as food
import src.items.armor as armor
import src.scripts.walk as walk
import json


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
            "Стейк": food.steak
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

if os.path.isfile("resource/stats.json"):
    load_data()
else:
    name = input("Назовите своего персонажа: ")
    main_hero = MainHero(weapon.stick, armor.bandage, 1, name, 0, 0)
    save_data()

walk.walk(main_hero)
save_data()
