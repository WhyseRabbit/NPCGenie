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
#             ]
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

statScores = {
    "Strength" : 10,
    "Dexterity" : 10,
    "Constitution" : 10,
    "Intelligence" : 10,
    "Wisdom" : 10,
    "Charisma" : 10
}

ancestry = {
    "Dwarf" : {
        "heritage" : {
            "Ancient-Blooded" : "Call on Ancient Blood",
            "Death Warden" : "Necromancy Ward",
            "Forge" : "Fire Resistance",
            "Rock" : "Firmly Grounded",
            "Strong-Blooded" : "Poison Resistance"
        },
        "HP" : 10,
        "size" : "Medium",
        "speed" : 20,
        statScores["Constitution"] : 12,
        statScores["Wisdom"] : 12,
        # random statScore increase here,
        statScores["Charisma"] : 8,
        "languages" : ["Common", "Dwarven"],
        "traits" : ["Dwarf", "Humanoid"],
        "ancestry feature" : "Darkvision"
    },
    
    "Elf" : {
        "heritage" : {
            "Arctic" : "Cold Resistance",
            "Cavern" : "Darkvision",
            "Seer" : "Magic Vision",
            "Whisper" : "Keen Hearing",
            "Woodland" : "Quick Climb"
        },
        "HP" : 6,
        "size" : "Medium",
        "speed" : 30,
        statScores["Dexterity"] : 12,
        statScores["Intelligence"] : 12,
        # random increase,
        statScores["Constitution"] : 8,
        "languages" : ["Common", "Elven"],
        "traits" : ["Elf", "Humanoid"],
        "ancestry feature" : "Low-Light Vision"
    },
    
    "Gnome" : {
        "heritage" : {
            "Chameleon" : "Blend In",
            "Fey-Touched" : "Fey Magic",
            "Sensate" : "Sharp Senses",
            "Umbral" : "Darkvision",
            "Wellspring" : "Wellspring Magic"
        },
        "HP" : 8,
        "size" : "Small",
        "speed" : 25,
        statScores["Constitution"] : 12,
        statScores["Charisma"] : 12,
        # random increase,
        statScores["Strength"] : 8,
        "languages" : ["Common", "Gnomish", "Sylvan"],
        "traits" : ["Gnome", "Humanoid"],
        "ancestry feature" : "Low-Light Vision"
    },
    
    "Goblin" : {
        "heritage" : {
            "Charhide" : "Fire Resistance",
            "Irongut" : "Affliction Resistance",
            "Razortooth" : "Bite Attack",
            "Snow" : "Cold Resistance",
            "Unbreakable" : "Hearty"
        },
        "HP" : 6,
        "size" : "Small",
        "speed" : 25,
        statScores["Dexterity"] : 12,
        statScores["Charisma"] : 12,
        # random increase,
        statScores["Wisdom"] : 8,
        "languages" : ["Common", "Goblin"],
        "traits" : ["Goblin", "Humanoid"],
        "ancestry feature" : "Darkvision"
    },
    
    "Halfling" : {
        "heritage" : {
            "Gutsy" : "Brave",
            "Hillock" : "Quick Healing",
            "Nomadic" : "Linguistics",
            "Twilight" : "Low-Light Vision",
            "Wildwood" : "Nimble Movement"
        },
        "HP" : 6,
        "size" : "Small",
        "speed" : 25,
        statScores["Dexterity"] : 12,
        statScores["Wisdom"] : 12,
        # random increase,
        statScores["Strength"] : 8,
        "languages" : ["Common", "Halfling"],
        "traits" : ["Halfling", "Humanoid"],
        "ancestry feature" : "Keen Eyes"
    }
}
