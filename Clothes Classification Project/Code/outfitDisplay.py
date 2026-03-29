from PIL import Image
from PIL import ImageDraw

from PIL import Image

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


# def show_outfit(outfit):
#     images = []

#     for i, img in enumerate(images):
#         draw = ImageDraw.Draw(img)
#         draw.text((10, 10), f"{i}", fill=(255, 0, 0))

#     for key in ["dress", "pant", "shoes", "shirt", "skirt"]:
#         if key in outfit:
#             img = Image.open(outfit[key])
#             img = img.resize((200, 200))
#             images.append(img)

#     if not images:
#         print("No outfit to display.")
#         return

#     # stack vertically
#     height = 200 * len(images)
#     final = Image.new("RGB", (200, height))

#     y_offset = 0
#     for img in images:
#         final.paste(img, (0, y_offset))
#         y_offset += 200

#     final.show()