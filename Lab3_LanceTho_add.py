"""
Lab3_LanceTho_add.py
Lance Thongsavanh
Import the list from your Lab3_username_list.py file. Do not copy and paste the list definition.
Append 5 more items to the imported list.
Print the resulting list reversed alphabetically.
1/28/2026
"""
import Lab3_LanceTho_list

Lab3_LanceTho_list.supplies.append("Lantern")
Lab3_LanceTho_list.supplies.append("Coat")
Lab3_LanceTho_list.supplies.append("Cooking Set")
Lab3_LanceTho_list.supplies.append("Clothes")
Lab3_LanceTho_list.supplies.append("Boots")

Lab3_LanceTho_list.supplies.sort()
Lab3_LanceTho_list.supplies.reverse()
print(f"List with 5 new items in reversed alphabetical order: {Lab3_LanceTho_list.supplies}")
