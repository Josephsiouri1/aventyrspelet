class Player():
    def __init__(self, name, strength, hp, inventory, level):
        self.name = name
        self.strength = strength
        self.hp = hp
        self.inventory = inventory
        self.level = level

    def new_hp(self, new_hp):
        self.hp = new_hp

    def new_level(self, new_level):
        self.level = new_level
