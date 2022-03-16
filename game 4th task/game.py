"""
file with classes
"""

class Room:
    """
    class Room
    """

    def __init__(self, room):
        """
        info about name
        >>> kitchen = Room("Kitchen")
        >>> kitchen.room
        'Kitchen'
        """
        self.room = room
        self.link_rom = {}
        self.set_descr = None
        self.character = None
        self.name = None

    def set_description(self, set_descr):
        """
        info about description
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_description(" ")
        """
        self.set_descr = set_descr

    def link_room(self, link_r, side):
        """
        info about link room
        """
        self.link_rom[side] = link_r

    def set_character(self, character):
        """
        info about in which room will be an enemy
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_character(" ")
        """
        self.character = character

    def get_character(self):
        """
        return name of the character
        """
        return self.character

    def set_item(self, name):
        """
        info about in which room will be an item
        >>> kitchen = Room("Kitchen")
        >>> kitchen.set_item('name')
        """
        self.name = name

    def get_item(self):
        """
        return name of the item
        >>> kitchen = Room("Kitchen")
        >>> kitchen.get_item()
        """
        return self.name

    def get_name(self):
        """
        return the name
        >>> kitchen = Room("Kitchen")
        >>> kitchen.get_name()
        'Kitchen'
        """
        return self.room

    def get_details(self):
        """
        prints the name of the room, '-' after the name of the room
        and in which side is another room
        """
        print(self.room)
        print('-'*20)
        print(self.set_descr)
        for side in self.link_rom:
            link_r = self.link_rom[side]
            print(f'The {link_r.get_name()} is {side}')

    def move(self, side):
        """
        returns information if player can go in the
        specified side
        >>> kitchen = Room("Kitchen")
        >>> kitchen.move('south')
        You can't go there
        """
        if side not in self.link_rom:
            print("You can't go there")
            return
        else:
            return self.link_rom[side]

class Enemy:
    """
    class Enemy
    """
    looses = 0

    def __init__(self, enemy, descr):
        """
        info about enemy
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.enemy
        'Dave'
        """
        self.enemy = enemy
        self.descr = descr
        self.conver = None
        self.weak = None

    def set_conversation(self, conver):
        """
        info about conversation
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_conversation("What's up, dude! I'm hungry.")
        """
        self.conver = conver

    def set_weakness(self, weak):
        """
        info about enemy's weaknesses
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("cheese")
        """
        self.weak = weak

    def talk(self):
        """
        if the option is 'talk'
        """
        if self.conver is not None:
            print(f'[{self.enemy} says]:{self.conver}')
        else:
            print()

    def fight(self, item):
        """
        if the option is fight
        """
        if item != self.weak:
            print(f'{self.enemy} crushes you, puny adventurer!')
            return False
        else:
            print(f'You fend {self.enemy }off with the {self.weak}')
            Enemy.looses += 1
            return True

    def get_defeated(self):
        """
        returns the number of enemy's looses
        """
        return Enemy.looses

    def describe(self):
        """
        prints if there is an enemy
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.describe()
        Dave is here!
        A smelly zombie
        """
        print(f'{self.enemy} is here!')
        print(self.descr)


class Item:
    """
    clas Item
    """

    def __init__(self, item):
        """
        info about room name
        >>> cheese = Item("cheese")
        >>> cheese.item
        'cheese'
        """
        self.item = item
        self.descr = None

    def set_description(self, descr):
        """
        description
        >>> cheese = Item("cheese")
        >>> cheese.set_description(" ")
        """
        self.descr = descr

    def get_name(self):
        """
        returns the name of the item
        >>> cheese = Item("cheese")
        >>> cheese.get_name()
        'cheese'
        """
        return self.item

    def describe(self):
        """
        prints the info about where is the item
        """
        print(f'The [{self.item}] is here - {self.descr}')
