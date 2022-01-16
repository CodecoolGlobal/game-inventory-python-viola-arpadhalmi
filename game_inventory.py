from operator import inv
import csv


def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    if inventory == '':
        return None
    else:
        for item, count in inventory.items():
            print(f'{item}: {count}')


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    if added_items not in inventory:
        inventory[added_items] = 1
    else:
        inventory[added_items] += 1


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    if removed_items in inventory:
        inventory[removed_items] -= 1
        if inventory[removed_items] <= 0:
            del inventory[removed_items]


def print_table(inventory, order=None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    DIVIDER = '-----------------'
    HEADER = 'item name | count'
    print(f'{DIVIDER}\n{HEADER}\n{DIVIDER}')
    if order == 'count,asc':
        for item, count in sorted(inventory).reverse():
            print(f'{item} |\t{count}')
    elif order == 'count,desc':
        for item, count in inventory.sort:
            print(f'{item} |\t{count}')
    else:
        for item, count in inventory.items():
            print(f'{item} |\t{count}')
    print(f'{DIVIDER}')


def import_inventory(inventory, filename='import_inventory.csv'):
    """Import new inventory items from a CSV file."""
    try:
        with open(filename, 'r') as csvfile:
            inventory_reader = csv.reader(csvfile)
            for row in inventory_reader:
                for i in row:
                    add_to_inventory(inventory, i)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_inventory(inventory, filename='export_inventory.csv'):
    """Export the inventory into a CSV file."""
    inventory_list = []
    for items, count in inventory.items():
        inventory_list.extend([items for i in range(count)])
    print(inventory_list)
    try:
        with open(filename, 'w') as export:
            writer = csv.writer(export)
            writer.writerow(inventory_list)
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")

inventory = {}
import_inventory(inventory, 'test_inventory.csv')
export_inventory(inventory)