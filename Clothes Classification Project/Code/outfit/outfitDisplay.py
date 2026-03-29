from PIL import Image, ImageTk
from pathlib import Path
import tkinter as tk

# def show_outfit(outfit):
#     images = []

#     # debugging print to check outfit contents
#     # print("DEBUG outfit:", outfit)

#     BASE_DIR = Path(__file__).resolve().parents[0]

#     for key in ["shirt", "pants", "skirt", "shoes", "dress"]:
#         if key in outfit:
#             img_path = BASE_DIR / outfit[key]

#             # debugging prints for missing files
#             # print("TRYING TO OPEN:", img_path)
#             # print("EXISTS:", img_path.exists())

#             if not img_path.exists():
#                 print(f"Missing file for {key}: {img_path}")
#                 continue

#             img = Image.open(img_path).resize((200, 200))
#             images.append(img)

#     if not images:
#         print("No outfit to display.")
#         return

#     final = Image.new("RGB", (200, 200 * len(images)))

#     for i, img in enumerate(images):
#         final.paste(img, (0, i * 200))

#     final.show()

def show_outfit_fullscreen(outfit):
    BASE_DIR = Path(__file__).resolve().parents[0]

    # 1. CREATE ROOT FIRST (this is the key fix)
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="white")

    images = []

    # 2. LOAD + ATTACH TO ROOT
    for key in ["shirt", "pants", "skirt", "shoes", "dress"]:
        if key in outfit:
            img_path = BASE_DIR / outfit[key]

            if img_path.exists():
                img = Image.open(img_path).resize((300, 300))
                photo = ImageTk.PhotoImage(img, master=root)
                images.append(photo)

                label = tk.Label(root, image=photo, bg="black")
                label.pack()

    if not images:
        print("No outfit to display.")
        root.destroy()
        return

    # 3. KEEP REFERENCES (VERY IMPORTANT)
    root.images = images

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()