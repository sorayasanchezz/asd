import sys


if __name__ == "__main__":
    argv = sys.argv[1:]
    inventory = {}

    print("=== Inventory System Analysis ===")

    # parse input
    for arg in argv:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name = parts[0]
        value = parts[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            inventory.update({name: int(value)})
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    # display inventory
    print(f"Got inventory: {inventory}")

    # item list
    items = list(inventory.keys())
    print(f"Item list: {items}")

    # total quantity
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    # percentages
    for name in inventory.keys():
        percent = inventory[name] * 100 / total
        print(f"Item {name} represents {percent:.1f}%")

    # most / least abundant
    first = True
    for name in inventory.keys():
        value = inventory[name]

        if first:
            most_name = name
            most_value = value
            least_name = name
            least_value = value
            first = False
        else:
            if value > most_value:
                most_name = name
                most_value = value
            if value < least_value:
                least_name = name
                least_value = value

    if len(inventory) > 0:
        print(f"Item most abundant: {most_name} with quantity {most_value}")
        print(f"Item least abundant: {least_name} with quantity {least_value}")

    # add new item
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
