from src.entity.MainHero import MainHero
import src.items.weapon as weapon
import src.items.food as food
import src.items.armor as armor
import src.scripts.walk as walk

main_hero = MainHero(weapon.stick, armor.bandage, 1, "Chara", 0)
main_hero.get_item(weapon.bow)
main_hero.get_item(food.apple)
main_hero.get_item(food.apple)
main_hero.get_item(food.apple)
main_hero.get_item(food.steak)
main_hero.get_item(food.steak)

walk.walk(main_hero)