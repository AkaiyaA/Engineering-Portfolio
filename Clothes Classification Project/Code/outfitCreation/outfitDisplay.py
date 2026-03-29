from PIL import Image
from PIL import ImageDraw

# from PIL import Image 

def show_outfit(outfit):
    images = []

    print("DEBUG outfit:", outfit)

    for key in ["shirt", "pants", "skirt", "shoes", "dress"]:
        if key in outfit:
            img = Image.open(outfit[key]).resize((200, 200))
            images.append(img)

    if not images:
        print("No outfit to display.")
        return

    final = Image.new("RGB", (200, 200 * len(images)))

    for i, img in enumerate(images):
        final.paste(img, (0, i * 200))

    final.show()

