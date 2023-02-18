#eating items does not work.
from adventurelib import when
from sys import exit
from charcter import *
from random import randint
import adventurelib as a

hit_points = 4
wizHitPoints = 20

userName = input("Please type your name: ")
print(f'Welcome {userName}')

raft = a.Room(
    """Thank you for playing. Note, sometimes lowercase is needed. You will want to use lowercase.
You wake up on a small raft in the middle of the ocean. You see a small bit of land in the west."""
)

island = a.Room("You are now on a small island with a faint trail")

town1 = a.Room(
    """You are now in a small village with people bustling on either side of you.
You realize that this is no island, is a continent."""
)

crossRoad = a.Room("""You find a small trail that goes north, east, and south.""")

cliff = a.Room(
    """As you climb the steep trail you see the ocean to the right of you. At the top,
you come to the end with a 100 foot cliff."""
)

ocean = a.Room("you see a small cave in the side of the cliff")

cave = a.Room(
    """In this small small cave, you hear water dripping. As you step in,
You step on a small stalagmite."""
)

fail = a.Room("""You find that the raft was not pulled up enough, so it floated away""")

tunnel = a.Room(
    """In the tunnel you hear water dripping in the far distance,
and what seems to be an underground river flowing through one part of the tunnel.
You see a small ladder on the edge of the wall."""
)

a.Room.add_direction("up", "down")


current_room = raft

raft.west = island
island.west = crossRoad
crossRoad.north = town1
crossRoad.south = cliff
island.east = fail
cave.north = tunnel
tunnel.up = town1


@when("go DIRECTION")
@when("s", direction="south")
@when("n", direction="north")
@when("e", direction="east")
@when("w", direction="west")
@when("up", direction="up")
def go(direction: str):
    """Processes your moving direction

    Arguments:
        direction {str} -- which direction does the player want to move
    """

    global current_room

    next_room = current_room.exit(direction)
    if next_room:
        current_room = next_room
        print(f"You go {direction}.")
        look()
    if hit_points < 1:
        exit()


@when("eat ITEM")
def eat(item: str):
    """Use an item, consumes it if used
    Arguments:
        item {str} -- Which item to use
    """

    obj = inventory.take(item)
    if obj.use_item(item):
        if item == sword:
            hit_points - 20000
        elif item == berrys or chocolate:
                hit_points + 2
        else: print(f"You can't eat {item}")

    else:
        not obj
        print(f"You don't have {item}")

@when("look")
def look():
    """Looks at the current room"""
    a.say(current_room)

    for item in current_room.contents:
        print(f"You see {item} here.")

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


@when("jump")
def jump():
    global current_room
    if current_room == cliff:
        current_room = ocean
        look()
    if hit_points < 1:
        exit()


@when("swim")
def swim():
    global current_room
    if current_room == ocean:
        current_room = cave
        look()
    else:
        print("You fall on your face trying to do a glories dive.")
        global hit_points
        hit_points -= 1
    if hit_points < 1:
        exit()


@when("talk to CHARACTER")
def talk_to(character: str):
    if character == "wizard":
        if current_room == town1:
            yes = input(
                """Do you want to go on a quest?
                        """
            )
            if yes == "yes":
                print(
                    """Okay. In this world there is a sword.
The one catch is, it's guarded by a giant lion. If you bring it to me,
I can enchant it for you."""
                )
            global cave
            cave.contents.add(sword)

        else:
            print("Who do you plan to talk to? the plants?")
    else:
        print("Well then. Come back when you feel like it!")


@when("attack CHARACTER")
def attack(character: str):
    if character == "wizard":
        yourDamage = randint(0, 4)
        yourDamage
        damage = randint(0, 3)
        damage -= hit_points
        if hit_points < 1:
            print("You died")
            exit()


@when("die")
def die():
    print("you died")
    exit()


@when("print health")
def print_health():
    global hit_points
    print(f"you have {hit_points} health!")
    if hit_points < 1:
        exit()


chocolate = a.Item("a small bar of chocolate", "chocolate")
chocolate.use_item = attack
berrys = a.Item("some shriveled berry's", "berry's")
berrys.use_item = attack
sword = a.Item("A gleaming sword", "sword")
sword.use_item = attack

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
fail.contents = a.Bag()
tunnel.contents = a.Bag()

inventory = a.Bag()


look()
a.start()



look()
a.start()
