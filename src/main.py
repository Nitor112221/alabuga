from src.entity.MainHero import MainHero
import src.items.weapon as weapon
import src.items.food as food
import src.items.armor as armor
import src.scripts.walk as walk

main_hero = MainHero(weapon.stick, armor.bandage, 1, "Chara", 0)

walk.walk(main_hero)