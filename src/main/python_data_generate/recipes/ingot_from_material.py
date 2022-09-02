import json

mod_metal = [
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
]

vanilla_metal = [
    'iron',
    'copper',
    'gold',
    'netherite'
]

for material in mod_metal :
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:dusts/" + material},
        "result": "omniores:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_dust/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:dusts/" + material},
        "result": "omniores:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_dust/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()


for material in vanilla_metal :
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:dusts/" + material},
        "result": "minecraft:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_dust/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:dusts/" + material},
        "result": "minecraft:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_dust/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()