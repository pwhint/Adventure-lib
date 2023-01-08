"""
Characters for the adventurelib Game
"""
from advRooms import userName

# Import the adventurelib library
import adventurelib as adv

# All characters have some properties
adv.Item.greeting = ""
adv.Item.context = ""

# Your characters
minotaur = adv.Item("hungry minotaur", "minotaur")
minotaur.description = """Almost four meters of hulking brutish strength
stands before you, his breath rank with rotten meat, his mangy hair
tangled and matted"""
minotaur.greeting = f"Ah. {userName}. Prepare to defend yourself!"
minotaur.context = "minotaur"