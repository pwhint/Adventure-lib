from adventurelib import when
from sys import exit
from charcter import *
import adventurelib as a


hit_points = 4

#userName = input("Please type your name: ")
#print(f'Welcome {userName}')

raft = a.Room("""Thank you for playing.
You wake up on a small raft in the middle of the ocean. You see a small bit of land in the west.""")

island = a.Room("You are now on a small island with a faint trail")

town1 = a.Room("""You are now in a small village with people bustling on either side of you.
You realize that this isno island, is a continent.""")

crossRoad = a.Room("""You find a small trail that goes north and south.""")

cliff = a.Room("""As you climb the steep trail you see the ocean to the right of you. At the top,
you come to the end with a 100 foot cliff.""")

ocean = a.Room("you see a small cave in the side of the cliff")

cave = a.Room(f"""In this small small cave, you hear water dripping. As you step in,
You step on a small stalagmite.""")

current_room = raft
#Making items
chocolate = a.Item("a small bar of chocolate", "chocolate")
berrys = a.Item("some shriveled berry's", "berry's")

raft.contents = a.Bag()
raft.contents.add(chocolate)

island.contents = a.Bag()
island.contents.add(berrys)

cliff.contents = a.Bag()

crossRoad.contents = a.Bag()

town1.contents = a.Bag()
town1.contents.add(wizard)

ocean.contents = a.Bag()

cave.contents = a.Bag()

inventory = a.Bag()

raft.west = island
island.north = town1
island.south = cliff

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

    next_room = current_room.exit(direction)
    if next_room:
        current_room = next_room
        print(f"You go {direction}.")
        look()
    if hit_points < 1:
        exit()

@when("look")
def look():
    """Looks at the current room"""
    # Describe the room
    a.say(current_room)

    # List the contents
    for item in current_room.contents:
        print(f"You see {item} here.")

    # List the exits
    print(f"The following exits are present: {current_room.exits()}")
    if hit_points < 1:
        exit()

@when("i")
def list_inventory():
    if inventory:
        print("You have the following items:")
        for item in inventory:
            print(f"  - {item}")
    else:
        print("You have nothing in your inventory.")
    if hit_points < 1:
        exit()

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
    if hit_points < 1:
        exit()

@when("eat ITEM")
def eat(item: str):
    if item:
        global hit_points
        hit_points += 1
        print(f"You ate {item}! You have {hit_points} health!")

    else:
        print(f"You can't eat {item}. Try again later when you have an edible item in you inventory.")
    if hit_points < 1:
        exit()

@when("jump")
def jump():
    global current_room
    if current_room == cliff:
        current_room = ocean
        look()
    if hit_points < 1:
        exit()

@when('swim')
def swim():
    global current_room
    if current_room == ocean:
        current_room = cave
    else:
        print("You fall on your face trying to do a glories dive.")
        global hit_points
        hit_points -=1
    if hit_points < 1:
        exit()

@when("talk CHARACTER")
def talk(character: str):
    if character == 'wizard':
        yes = input("""Do you want to go on a quest?
                    """)
        if yes == 'yes':
            print("""Okay. In this world there is a magic sword.
The one catch is, it's guarded by a giant lion.""")
        else:
            print("Well then. Come back when you feel like it!")
    else:
        print("Who do you plan to talk to? the plants?")


@when('die')
def die():
    print("you died")
    exit()

@when("print health")
def print_health():
    global hit_points
    print(f"you have {hit_points} health!")
    if hit_points < 1:
        exit()

look()
a.start()
