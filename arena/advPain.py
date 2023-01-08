import adventurelib as adv
from adventurelib import when
from advRooms import *
from advChat import minotaur
import random

hp = 20
toHit = 8
attacking = False
defending = False
minotaurHealth = 30

current_room = prison

@when("print health")
def health():
    global hp
    print(hp)

@when("print hit points")
def hitPoints():
    global toHit
    print(toHit)

@when("attack CHARACTER")
def attack(character):
    if current_room == arena:
        useWeaponInput = input("Are you sure you want to attack? ")
        if useWeaponInput == "yes":
            print(f"Okay! Now kill the {character}.")
            

@when("eat ITEM")
def eat(item: str):
    global crumbs
    if item == 'crumbs':
        global hp
        hp += 1
        print(f"You ate {item}! You have {hp} health!")

    else:
        print(f"You can't eat {item}. Try again later when you have an edible item in you inventory.")

@when("wear ITEM")
def wear(item: str):
    if item == 'shield':
        global defending
        global toHit
        defending = True
        print(f"You are wearing a {item}!")
        toHit += 3
    else:
        print(f"you are trying to wear a {item}? how do you attend to that?")

sword = adv.Item("a small rusty sword", "sword")
sword.use_item = attack

axe = adv.Item("a axe more suited for chopping trees than enemies", "axe")
axe.use_item = attack

shield = adv.Item("a large buckler with rawhide over wood", "shield", "buckler")
shield.use_item = wear

crumbs = adv.Item("some crumbs", "crumbs")
crumbs.use_item = eat

prison.contents = adv.Bag()
armory.contents = adv.Bag()
arena.contents = adv.Bag()

arena.locked = dict()
armory.locked = dict()
prison.locked = dict()

armory.contents.add(sword)
#armory.contents.add(axe)
armory.contents.add(shield)
prison.contents.add(crumbs)

prison.south = armory
armory.west = arena

inventory = adv.Bag()

@when("go DIRECTION")
@when("s", direction = "south")
@when("n", direction = "north")
@when("e", direction = "east")
@when("w", direction = "west")

def go(direction: str):
    """Processes your moving direction

    Arguments:
        direction {str} -- which direction does the player want to move
    """

    # What is your current room?
    global current_room

    # Is there an exit in that direction?
    next_room = current_room.exit(direction)
    if next_room:
        # Is the door locked?
        if direction in current_room.locked and current_room.locked[direction]:
            print(f"You can't go {direction} --- the door is locked.")
        else:
            current_room = next_room
            print(f"You go {direction}.")
            look()

# How do you look at the room?
@when("look")
def look():
    """Looks at the current room"""

    # Describe the room
    adv.say(current_room)

    # List the contents
    for item in current_room.contents:
        print(f"There is {item} here.")

    # List the exits
    print(f"The following exits are present: {current_room.exits()}")

@when("i")
def list_inventory():
    if inventory:
        print("You have the following items:")
        for item in inventory:
            print(f"  - {item}")
    else:
        print("You have nothing in your inventory.")

# How do you look at items?
@when("look at ITEM")
def look_at(item: str):

    # Check if the item is in your inventory or not
    obj = inventory.find(item)
    if not obj:
        print(f"You don't have {item}.")
    else:
        print(f"It's an {obj}.")

# How do you pick up items?
@when("take ITEM")
@when("get ITEM")
def get(item: str):
    """Get the item if it exists

    Arguments:
        item {str} -- The name of the item to get
    """
    global current_room

    obj = current_room.contents.take(item)
    if not obj:
        print(f"There is no {item} here.")
    else:
        print(f"You now have {item}.")
        inventory.add(obj)

# How do you use an item?

if __name__ == "__main__":
    # Look at the starting room
    look()

    adv.start()

adv.start()