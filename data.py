from random import randint, randrange

# Currently, for the sake of saving time, region will be limited to Avistan
# Using this site as inspiration/template:
# https://python.plainenglish.io/lets-build-a-random-character-generator-in-python-7f2f42bea5d1

# Seperating names and races as names will be 3 or more parts added together

"""
To be built from the ground up, this project needs better planning
"""
# regionalNames = {
#     "Human" : 
#     {
#         "first names" : 
#         {
#             "Absalom" : [],
#             "Andoran" : [],
#             "Brevoy" : [],
#             "Cheliax" : [],
#             "Druma" : [],
#             "Galt" : [],
#             "Hermea" : [],
#             "Hold of the Bekzen" : [],
#             "Irrisen" : [],
#             "Isger" : [],
#             "Lastwall" : [],
#             "Lands of the Linnorm Kings" : [],
#             "Mendev" : [],
#             "Molthune" : [],
#             "Nidal" : [],
#             "Nirmathas" : [],
#             "Numeria" : [],
#             "Qadira" : [],
#             "Razmiran" : [],
#             "Realm of the Mammoth Lords" : [],
#             "The River Kingdoms" : [],
#             "Taldor" : [],
#             "Ustalav" : [],
#             "Varisia" : [],
#             "Worldwound" : []
#         },
#         "Last names" : 
#         {
#             "Absalom" : [],
#             "Andoran" : [],
#             "Brevoy" : [],
#             "Cheliax" : [],
#             "Druma" : [],
#             "Galt" : [],
#             "Hermea" : [],
#             "Hold of Belkzen" : [],
#             "Irrisen" : [],
#             "Isger" : [],
#             "Lastwall" : [],
#             "Lands of the Linnorm Kings" : [],
#             "Mendev" : [],
#             "Molthune" : [],
#             "Nidal" : [],
#             "Nirmathas" : [],
#             "Numeria" : [],
#             "Qadira" : [],
#             "Razmiran" : [],
#             "Realm of the Mammoth Lords" : [],
#             "The River Kingdoms" : [],
#             "Taldor" : [],
#             "Ustalav" : [],
#             "Varisia" : [],
#             "Worldwound" : []
#         },
#         "region" : [
#             "Absalom", "Andoran", "Brevoy", "Cheliax", "Druma", "Galt", "Hermea",
#             "Hold of Belkzen", "Irrisen", "Isger", "Lastwall", "Lands of the Linnorm Kings",
#             "Mendev", "Molthune", "Nidal", "Nirmathas", "Numeria", "Qadira", "Razmiran",
#             "Realm of the Mammoth Lords","The River Kingdomes", "Taldor", "Ustalav",
#             "Varisia", "Worldwound"
#             ],
#         "age" : randint(7, 95),
#         "height" : randint(60, 80),
#         "weight" : randint(120, 160),
#         "size" : "Medium",
#         "speed" : 25
#     }
# }


# classes = {
#     "Alchemist" : {
#         "stats" : 
#     }
# }

"""
All stats start at 10 and get increased by the choices generated.
"""

ancestry = {
    "Dwarf" : {
        "heritage" : [
            "Ancient-Blooded", "Death Warden",
            "Forge", "Rock", "Strong-Blooded"
            ],
        "HP" : 10,
        "speed" : 20,
    }
}
