import json

metal = [
    "tin",
    "lead",
    "nickel",
    "zinc",
    "aluminum",
    "silver",
    "cobalt",
    "osmium",
    "iridium",
    "uranium",
    "bronze",
    "brass",
    "steel",
    "electrum",
    "invar",
    "constantan",
    "signalum",
    "lumium",
    "enderium",
    'iron',
    'copper',
    'gold',
    'netherite'
]

gem = [
    'diamond',
    'emerald',
    "ruby",
    "sapphire",
    'quartz',
    'lapis'
]

for material in metal :
    recipe_rod = {
        "type": "minecraft:crafting_shaped",
        "pattern": ['#', '#'],
        "key": {"#": {"tag": "forge:ingots/" + material}},
        "result": {"item": "omniores:" + material + "_rod", "count": 2}
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/rod_from_material/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe_rod, indent=2))
    file.close()


    recipe_gear = {
        "type": "minecraft:crafting_shaped",
        "pattern": [' # ', '#I#', ' # '],
        "key": {
            "#": {"tag": "forge:ingots/" + material},
            "I": {"tag": "forge:nuggets/iron"}
            },
        "result": {"item": "omniores:" + material + "_gear"}
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/gear_from_material/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe_gear, indent=2))
    file.close

for material in gem :
    recipe_rod = {
        "type": "minecraft:crafting_shaped",
        "pattern": ['#', '#'],
        "key": {"#": {"tag": "forge:gems/" + material}},
        "result": {"item": "omniores:" + material + "_rod", "count": 2}
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/rod_from_material/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe_rod, indent=2))
    file.close()


    recipe_gear = {
        "type": "minecraft:crafting_shaped",
        "pattern": [' # ', '#I#', ' # '],
        "key": {
            "#": {"tag": "forge:gems/" + material},
            "I": {"tag": "forge:nuggets/iron"}
            },
        "result": {"item": "omniores:" + material + "_gear"}
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/gear_from_material/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe_gear, indent=2))
    file.close