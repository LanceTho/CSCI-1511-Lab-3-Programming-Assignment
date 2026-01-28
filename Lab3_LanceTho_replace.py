"""
Lab3_LanceTho_replace.py
Lance Thongsavanh
Import the list from your Lab3_username_add.py file.
Replace one of the string items from the list with "binoculars", but don't replace the first or the last element in the list.
    Using Slice Notation,
    print the list from the start of the list to the binoculars item(not including the binoculars),
    the binoculars,
    and the list from the first item after the binoculars to the end of the list
1/28/2026
"""

import Lab3_LanceTho_add

Lab3_LanceTho_add.Lab3_LanceTho_list.supplies.insert(4, "binoculars")
Lab3_LanceTho_add.Lab3_LanceTho_list.supplies.pop(5)
print(f"Start of the list before 'binoculars': {Lab3_LanceTho_add.Lab3_LanceTho_list.supplies[0:4]}")
print(f"{Lab3_LanceTho_add.Lab3_LanceTho_list.supplies[4:5]}")
print(f"Rest of the list: {Lab3_LanceTho_add.Lab3_LanceTho_list.supplies[5:]}")