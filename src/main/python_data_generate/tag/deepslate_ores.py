import json

materials = [
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

deepslateList = []

for material in materials :
    # tagFile = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ores_in_ground/deepslate/' + material + '.json', 'w')
    # tagJson = {
    #     "replace": False,
    #     "values": ['omniores:' + material + '_ore_deepslate']
    # }
    # tagFile.write(json.dumps(tagJson))
    # tagFile.close()

    deepslateList.append('omniores:' + material + '_ore_deepslate')

deepslateJson = {
    "replace": False,
    "values": deepslateList
}
deepslateFile = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ores_in_ground/deepslate.json', 'w')
deepslateFile.write(json.dumps(deepslateJson, indent=2))
deepslateFile.close()