#!/usr/bin/env python3

#!/usr/bin/env python3

import sys

def ft_inventory_system() -> None:
    elem_inventory = {}

    print("=== Inventory System Analysis ===")

    for argc in sys.argv[1:]:
        if argc.count(":") != 1:
            print(f"Error - invalid parameter '{argc}'")
            continue

        item_name, qty_str = argc.split(":")

        if item_name in elem_inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(qty_str)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue

        elem_inventory[item_name] = quantity

    print(f"Got inventory: {elem_inventory}")

    items_list = list(elem_inventory.keys())
    print(f"Item list: {items_list}")

    total_values = sum(elem_inventory.values())
    print(f"Total quantity of the {len(elem_inventory)} items: {total_values}")

    if total_values > 0:
        for item_name in elem_inventory:
            quantity = elem_inventory[item_name]
            percent = round((quantity / total_values) * 100, 1)
            print(f"Item {item_name} represents {percent}%")

    if len(elem_inventory) > 0:
        first_item = items_list[0]
        max_item = first_item
        min_item = first_item

        for item in elem_inventory:
            if elem_inventory[item] > elem_inventory[max_item]:
                max_item = item
            if elem_inventory[item] < elem_inventory[min_item]:
                min_item = item

        print(f"Item most abundant: {max_item} with quantity {elem_inventory[max_item]}")
        print(f"Item least abundant: {min_item} with quantity {elem_inventory[min_item]}")

    elem_inventory.update({"magic_item": 1})
    print(f"Updated inventory: {elem_inventory}")


if __name__ == "__main__":
    ft_inventory_system()
