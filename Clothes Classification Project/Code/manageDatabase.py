

from database import get_clothes, delete_clothing

items = get_clothes()

print("Current items:")
for item in items:
    print(item)

item_id = int(input("Enter ID to delete (0 to exit): "))
while item_id != 0:
    delete_clothing(item_id)
    print("Deleted. Current items:")
    items = get_clothes()
    for item in items:
        print(item)
    item_id = int(input("Enter ID to delete (0 to exit): "))

print("Deleted.")