# runOutfit.py

from outfitGen import get_clothes, group_clothes, generate_outfit
from outfitDisplay import show_outfit

items = get_clothes()
wardrobe = group_clothes(items)
outfit = generate_outfit(wardrobe)

print("Generated Outfit:")
for k, v in outfit.items():
    print(f"{k}: {v}")

show_outfit(outfit)

