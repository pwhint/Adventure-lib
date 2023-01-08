from adventurelib import when
from adventurelib import Room
userName = input("Please enter you name: ")
prison = Room(f"""
Welcome to the Roman time survival game {userName}. you are in a small cell. All there is, is a small empty tray of food, some chains and shackles are on your ankles.
Outside of your cell you hear a booming voice. saying \"Oh! Billy Bob is on the ground. Joe comes for the finishing hit!\"
You hear assorted groans and cheers from what seem to be a massive audience. A guard comes and says: \"Come. Time to come and pick your weapon.\"""")
armory = Room("""
In the armory you see assorted thing on the rack. Somehow you know not to choose multiple weapons. Suddenly the guard says.
\"You may choose one large weapon and one small one. A shield counts as one small weapon\"""")
arena = Room(f"""
You are led by a rope on your neck to a large arena. Seeing a large crowd, you know that this will be a fight to the death.
On a raised dais you see a large man with a gleaming crown. You start hearing the chant, {userName}, {userName}, {userName}.
Then you see a large bull being led into the arena. Taking a closer look, you see that it is part man, part bull.
The Minotaur.""")