inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


#displays the inventory
def display_inventory(inventory):
    total = 0
    print ("Inventory:")
    for i in inventory:
        print (inventory[i], i)
        total += inventory[i]
    print ("Total number of items:", total)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#updating the inventory
def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

#prints out the inventory, adjusting rows and columns and handling whitespace
def printed(order, scale):
        print ("Inventory:")
        print (" " * (7 - len("count")) + "count" + " " *
               (4 + len(max(inv, key=len)) - len("item name")) + "item name")
        print ("-" * (11 + len(max(inv, key=len))))
        total = 0
        if order is not None:
            for i in sorted(inv, key=inv.get, reverse=scale):
                print (" " * (7 - len(str(inv[i]))) + str(inv[i]) + " " * (
                    4 + len(max(inv, key=len)) - len(i.rstrip())) + i.rstrip())
                total += inv[i]
        else:
            for i in inv:
                print (" " * (7 - len(str(inv[i]))) + str(inv[i]) + " " * (
                    4 + len(max(inv, key=len)) - len(i.rstrip())) + i.rstrip())
                total += inv[i]
        print ("-" * (11 + len(max(inv, key=len))))
        print ("Total number of items:", total)

#prints out tables ordered by count
def print_table(order=None):
    if order is None:
        printed(None, None)
    elif order == "count,desc":
        printed("count,desc", True)
    elif order == "count,asc":
        printed("count,asc", False)

#importing from a file, handling whitespace
def import_inventory(filename="import_inventory.csv"):
    inventory_file = open(filename, "a+")
    inventory_file.seek(0)
    x = 0
    get_item = []
    for line in inventory_file:
        x += 1
        if x > 1:
            if "\t" in line:
                line = (line.rstrip("\n")).split(",")
                for n in range(int(line[1])):
                    get_item.append(line[0].replace("\t", "  "))

            else:
                line = (line.rstrip("\n")).split(",")
                for n in range(int(line[1])):
                    get_item.append(line[0])
    add_to_inventory(inv, get_item)

import_inventory()

#exporting to a file
def export_inventory(filename="export_inventory.csv"):
    inventory_export = open(filename, "w+")
    inventory_export.writelines("item_name" + "," + "count" + "\n")
    for n in inv:
        inventory_export.writelines(n + "," + str(inv[n]) + "\n")

export_inventory()
print_table("count,asc")
