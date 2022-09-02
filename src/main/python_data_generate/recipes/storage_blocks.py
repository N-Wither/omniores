import json

materials_metal = [
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

materials_gem = [
    "ruby",
    "sapphire",
    "sulfur",
    "cinnabar",
    "potassium_nitrate",
    "apatite",
    "fluorite",
    "coal_coke",
]

for material in materials_metal:
    recipe = {
        "type": "minecraft:crafting_shaped",
        "group": "omniores",
        "pattern": ["###", "###", "###"],
        "key": {"#": {"tag": "forge:ingots/" + material}},
        "result": {"item": "omniores:" + material + "_block"},
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/block_from_material/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close

for material in materials_metal:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "group": "omniores",
        "ingredients": [{"tag": "forge:storage_blocks/" + material}],
        "result": {"item": "omniores:"+material+"_ingot", "count": 9},
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_block/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close

for material in materials_gem:
    recipe = {
        "type": "minecraft:crafting_shaped",
        "group": "omniores",
        "pattern": ["###", "###", "###"],
        "key": {"#": {"tag": "forge:gems/" + material}},
        "result": {"item": "omniores:" + material + "_block"},
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/block_from_material/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close

for material in materials_gem:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "group": "omniores",
        "ingredients": [{"tag": "forge:storage_blocks/" + material}],
        "result": {"item": "omniores:"+material+"_gem", "count": 9},
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/material_from_block/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close