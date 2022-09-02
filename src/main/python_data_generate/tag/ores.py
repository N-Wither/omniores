import json

ores = [
    'iron',
    'coal',
    'gold',
    'copper',
    'silver',
    'redstone',
    'diamond',
    'lapis',
    'emerald',
    'quartz',
    'tin',
    'lead',
    'nickel',
    'zinc',
    'aluminum',
    'cobalt',
    'osmium',
    'iridium',
    'uranium',
    'ruby',
    'sapphire',
    'sulfur',
    'cinnabar',
    'potassium_nitrate',
    'apatite',
    'fluorite'
]

stones = [
    'andesite',
    'basalt',
    'blackstone',
    'calcite',
    'deepslate',
    'diorite',
    'end_stone',
    'granite',
    'netherrack',
    'stone',
    'tuff',
    'create_limestone',
    'create_scoria',
    'create_scorchia',
    'quark_jasper',
    'quark_limestone',
    'quark_shale'
]

forge_ores = {
    "replace": False,
    "values" : []
}

forge_ores_specific = {
    "raplace": False,
    "values": []
}

for ore in ores :
    for stone in stones :
        forge_ores["values"].append('omniores:' + ore + '_ore_' + stone)
        forge_ores_specific["values"].append('omniores:' + ore + '_ore_' + stone)
    block_forge_ores_specific = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/blocks/ores/'+ore+'.json', 'w')
    block_forge_ores_specific.write(json.dumps(forge_ores_specific, indent=2))
    block_forge_ores_specific.close()
    item_forge_ores_specific = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ores/'+ore+'.json', 'w')
    item_forge_ores_specific.write(json.dumps(forge_ores_specific, indent=2))
    item_forge_ores_specific.close()
    forge_ores_specific['values'] = []

block_forge_ores_file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/blocks/ores.json', 'w')
block_forge_ores_file.write(json.dumps(forge_ores, indent=2))
block_forge_ores_file.close()

item_forge_ores_file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ores.json', 'w')
item_forge_ores_file.write(json.dumps(forge_ores, indent=2))
item_forge_ores_file.close()