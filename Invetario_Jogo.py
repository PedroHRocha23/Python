
# Inventário atual do jogador
inventory = {'rope': 1,'torch': 6,'gold coin': 42,'dagger': 1,'arrow': 12,}

# Mostrar o inventários do jogador
def displayInventory(inventory):
    counter = 0
    print('Inventory:')
    for k,v in inventory.items():
        counter += v
        print(f'{v} {k}')

    print(f'Total number of itens: {counter}')

# Incluindo itens ao inventário.
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']

def addToInventory(inventory, loot):
    for item in loot:
        if item in inventory.keys():
            inventory[item] += 1
        if item not in inventory.keys():
            inventory.setdefault(item, 1)

    return inventory

# Função principal
def main():
    displayInventory(inventory)
    x = addToInventory(inventory, dragonLoot)
    displayInventory(x)

main()
