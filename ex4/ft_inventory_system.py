import sys


def get_total_items(inventory: dict[str, int]) -> int:
    total = 0
    for value in inventory.values():
        total += value
    return total


def inventory_analysis(inventory: dict[str, int]) -> None:
    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", get_total_items(inventory))
    print("Unique item types:", len(inventory))


def show_sorted_inventory(inventory: dict[str, int]) -> None:
    """Print all inventory items from highest to lowest quantity"""

    print("=== Current Inventory ===")
    total_items = get_total_items(inventory)
    printed: dict[str, bool] = dict()
    i = 0

    # Iterate len(inventory) times, each time printing the highest value
    while i < len(inventory):
        end_value = -1
        end_name = ""

        # Separate values
        for name, value in inventory.items():
            # Compare all values saving the highest value
            # If it has not been printed
            if value > end_value and not printed.get(name):
                end_name = name
                end_value = value

        printed.update({end_name: True})
        percent = (end_value / total_items) * 100
        if end_value == 1:
            print(f"{end_name}: {end_value} unit ({percent:.1f}%)")
        else:
            print(f"{end_name}: {end_value} units ({percent:.1f}%)")
        i += 1


def inventory_statistics(inventory: dict[str, int]) -> None:
    """Search the highest and lowest value item"""
    print("=== Inventory Statistics ===")
    first = True

    # Iterates, compare and save the highest and lowest value
    for name, value in inventory.items():
        # If this is the first iteration, initialize the values
        if first:
            most_name = name
            most_value = value
            least_name = name
            least_value = value
            first = False
        # Compare for “less than” and “greater than”
        else:
            if most_value < value:
                most_value = value
                most_name = name
            if least_value > value:
                least_value = value
                least_name = name

    if most_value == 1:
        print(f"Most abundant: {most_name} ({most_value} unit)")
    else:
        print(f"Most abundant: {most_name} ({most_value} units)")

    if least_value == 1:
        print(f"Least abundant: {least_name} ({least_value} unit)")
    else:
        print(f"Least abundant: {least_name} ({least_value} units)")


def item_categories(inventory: dict[str, int]) -> None:
    """Separate items by category (value >= 5)"""
    print("=== Item Categories ===")

    # Dictiorary that contains other dictionaries
    categories: dict[str, dict[str, int]] = {
        "Moderate": {},
        "Scarce": {}
    }

    # Iterates and save values in different categories
    for name, value in inventory.items():
        if value >= 5:
            categories["Moderate"].update({name: value})
        else:
            categories["Scarce"].update({name: value})

    print("Moderate:", categories["Moderate"])
    print("Scarce:", categories["Scarce"])


def management_suggestions(inventory: dict[str, int]) -> None:
    """Save name for items with (value == 1), and request restock"""
    print("=== Management Suggestions ===")
    text = ""
    printed = False

    # Added items in the text to print
    for name, value in inventory.items():
        if value <= 1:
            if printed:
                text += ", "
            text += name
            printed = True

    print("Restock needed:", text)


def sample_lookup(inventory: dict[str, int], item: str) -> None:
    """Check if an item is in inventory,
    whether it exists or not, it is displayed"""
    print(f"Sample lookup - '{item}' in inventory:", item in inventory)


def dictionary_properties_demo(inventory: dict[str, int]) -> None:
    print("=== Dictionary Properties Demo ===")
    text_keys = ""
    printed_keys = False
    text_values = ""
    printed_values = False

    # Added items in the text to print
    for name, value in inventory.items():
        if printed_keys:
            text_keys += ", "
        if printed_values:
            text_values += ", "

        text_keys += name
        text_values += f"{value}"
        printed_keys = True
        printed_values = True

    print("Dictionary keys:", text_keys)
    print("Dictionary values:", text_values)
    sample_lookup(inventory, "sword")


if __name__ == "__main__":
    argv = sys.argv[1:]
    inventory = dict()

    try:
        # Add items (input) in inventory
        for arg in argv:
            name, value = arg.split(":")
            inventory.update({name: int(value)})

        if len(inventory) > 0:
            inventory_analysis(inventory)
            print()
            show_sorted_inventory(inventory)
            print()
            inventory_statistics(inventory)
            print()
            item_categories(inventory)
            print()
            management_suggestions(inventory)
            print()
            dictionary_properties_demo(inventory)
    except ValueError as e:
        print(f"{e}")
