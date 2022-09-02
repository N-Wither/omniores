import json

materials = [
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
    "enderium"
]

for material in materials :
    recipe = {
        'type': 'minecraft:crafting_shaped',
        'group': 'omniores',
        'pattern': ['###', '###', '###'],
        'key': {'#': {'tag': 'forge:nuggets/'+material}},
        'result': {'item': 'omniores:'+material+'_ingot'}
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/ingot_from_nugget/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close

for material in materials :
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "group": "omniores",
        "ingredients": [{"tag": "forge:ingots/" + material}],
        "result": {"item": "omniores:"+material+"_nugget", "count": 9}
    }
    file = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/recipes/nugget_from_ingot/"
        + material
        + ".json",
        "w",
    )
    file.write(json.dumps(recipe, indent=2))
    file.close