# Lab-4

Desription of the game:

Game space is created by creating rooms with a name and description. The mutual arrangement of rooms is arranged around the world. The rooms house the characters of the game, as well as items that you can try to use to fight enemies. It also determines how the character will respond to an attempt to talk to him and the object that can defeat the enemy.

After building the playing field, the location of the player who has an empty backpack where he can put items to fight enemies is established.

The main cycle of the program is executed until the player dies or two enemies die. The main cycle displays information about the current room, the characters that are there and objects in this room. The player can choose one of the following steps: go to another room, pick up an item, start a conversation or start a fight.

If a player picks up an item, it disappears from the room and appears in the player's backpack. If the player chooses the direction in which the other room is located, this room becomes the current room and the game continues. If the player starts a conversation, a message from the character is displayed on the screen. Fighting the enemy begins with entering the name of the object to fight, if such an object is in the backpack and it is such an object that can be won, the player is credited with the first victory (the game lasts up to two victories). If the item is not suitable for fighting this enemy, the player is credited with defeat.

Short description of the file wih classes:

There are only 3 classes: Room, Enemy and Item. In the first one we give an info about rooms, their location relative to other rooms, descriptions of theese rooms, in which room an enemy and item is located, the function if the player can go in the selected direction and the function, which adds some details in the game(name of the room and some description)

The class Enemy describes an info about enemies, which replics will the tell us, their weaknesses, function, which counts enemy's looses. There also are 2 functions, which describe what will happend if we will choose to talk, or to fight

The last one called Item has an information about description of items(weaknesses of the enemy)and their names. 
