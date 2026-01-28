"""
Lab3_LanceTho_list.py
Lance Thongsavanh
Create a list of strings containing exactly 10 items you are taking with you (e.g., "tent poles").
Print the total number of items in your list.
Print the list sorted alphabetically.
1/28/2026
"""
#create a list of items to take on a camping trip
supplies: list = ["Firestarter", "Backpack", "Tent", "First Aid Kit", "Sleeping Bag", "Water Bottle", "Folding Chair", "Flashlight", "Pillow", "Pocket Knife"]

#print the list unsorted
print(f"Unsorted list: {supplies}")

#sorts the list alphabetically
supplies.sort()

#print the newly sorted list
print(f"Sorted list: {supplies}")