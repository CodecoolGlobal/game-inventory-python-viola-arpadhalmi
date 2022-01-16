
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


from operator import inv


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
            print(f'{item}\t|\t{count}')
    elif order == 'count,desc':
        for item, count in sorted(inventory.items()):
            print(f'{item}\t|\t{count}')
    else:
        for item, count in inventory.items():
            print(f'{item}\t|\t{count}')
    print(f'{DIVIDER}')


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
