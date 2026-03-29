# runOutfit.py

from outfitGen import get_clothes, group_clothes, generate_outfit
# from outfitDisplay import show_outfit
from outfitDisplay import show_outfit_fullscreen



items = get_clothes()
wardrobe = group_clothes(items)
outfit = generate_outfit(wardrobe)

# debugging print to check outfit contents
# print("Generated Outfit:")
# for k, v in outfit.items():
#     print(f"{k}: {v}")

show_outfit_fullscreen(outfit)

# show_outfit(outfit)

