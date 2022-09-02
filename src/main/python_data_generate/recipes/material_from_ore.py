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
]

mod_gem = [
    "ruby",
    "sapphire",
    "sulfur",
    "cinnabar",
    "potassium_nitrate",
    "apatite",
    "fluorite",
]

vanilla_metal = ["iron", "copper", "gold"]

vanilla_gem = ["diamond", "emerald", "redstone", "coal", "quartz", "lapis"]

for material in mod_metal:
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "omniores:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:raw_materials/" + material},
        "result": "omniores:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_raw/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "omniores:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:raw_materials/" + material},
        "result": "omniores:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_raw/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

for material in mod_gem:
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "omniores:"+material+"_gem",
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "omniores:"+material+"_gem",
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

for material in vanilla_metal:
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "minecraft:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "minecraft:"+material+"_ingot",
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()


for material in vanilla_gem:
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "minecraft:"+material,
        "experience": 0.7,
        "cookingtime": 200,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/smelt/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()

    recipe = {
        "type": "minecraft:blasting",
        "ingredient": {"tag": "forge:ores/" + material},
        "result": "minecraft:"+material,
        "experience": 0.7,
        "cookingtime": 100,
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_ore/blast/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close()
