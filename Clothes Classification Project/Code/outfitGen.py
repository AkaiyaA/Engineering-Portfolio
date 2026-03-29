# outfitGen.py


from database import get_clothes
from collections import defaultdict
import random

def group_clothes(items):
    wardrobe = defaultdict(list)

    for _, class_name, image in items:
        wardrobe[class_name].append(image)

    class_name = class_name.lower().strip()

    print("RAW ITEMS:", items)
    print("WARDROBE:", wardrobe)

    return wardrobe

def generate_outfit(wardrobe):
    outfit = {}

    # tops
    if wardrobe.get("shirt"):
        outfit["shirt"] = random.choice(wardrobe["shirt"])

    # bottoms
    if wardrobe.get("pants"):
        outfit["pants"] = random.choice(wardrobe["pants"])
    elif wardrobe.get("skirt"):
        outfit["skirt"] = random.choice(wardrobe["skirt"])

    # shoes
    if wardrobe.get("shoes"):
        outfit["shoes"] = random.choice(wardrobe["shoes"])

    print("WARDROBE KEYS:", list(wardrobe.keys()))
    print("OUTFIT:", outfit)

    return outfit
