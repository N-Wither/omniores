import json

blocks = [
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
    "ruby",
    "sapphire",
    "sulfur",
    "cinnabar",
    "potassium_nitrate",
    "apatite",
    "fluorite",
    "coal_coke",
    "charcoal",
]

for block in blocks:
    loot = {
            "type": "minecraft:block",
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": "omniores:%s_block" % (block),
                        }
                    ],
                    "conditions": [{"condition": "minecraft:survives_explosion"}],
                }
            ],
        }
    
    table = open(
        "F:/Creative/diversityMods/omniores/src/main/resources/data/omniores/loot_tables/blocks/"
        + block
        + "_block.json",
        "w",
    )
    table.write(json.dumps(loot, indent=2))
    table.close()
