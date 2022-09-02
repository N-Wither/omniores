import json

materials_metal = [
    'iron',
    'copper',
    'gold',
    'tin',
    'lead',
    'nickel',
    'zinc',
    'aluminum',
    'silver',
    'cobalt',
    'osmium',
    'iridium',
    'uranium',
    'bronze',
    'brass',
    'steel',
    'electrum',
    'invar',
    'constantan',
    'signalum',
    'lumium',
    'enderium',
    'netherite'
]

materials_gem = [
    # 'lapis',
    # 'diamond',
    # 'emerald',
    # 'ruby',
    # 'sapphire',
    # 'coal',
    # 'sulfur',
    # 'cinnabar',
    # 'potassium_nitrate',
    # 'apatite',
    # 'fluorite',
    # 'coal_coke',
    # 'coal',
    # 'sulfur',
    # 'cinnabar',
    # 'potassium_nitrate',
    # 'apatite',
    # 'fluorite'
]

items = [
    'ingot',
    'nugget',
    'dust',
    'plate',
    'rod',
    'gear'
]

items_gem = [
    'dust',
    'plate',
    'rod',
    'gear',
    'gem'
]


for material in materials_metal :
    model_file = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/models/item/' + 'raw_' + material + '.json', 'w')
    model_file.write(json.dumps({"parent": "minecraft:item/generated","textures": {"layer0": "omniores:item/raw_%s" % (material)}}, indent=2))
    model_file.close()
    for item in items :
        model = {
            "parent": "minecraft:item/generated",
            "textures": {
            "layer0": "omniores:item/%s_%s" % (material, item)
            }
        }
        model_file = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/models/item/' + material + '_' + item + '.json', 'w')
        model_file.write(json.dumps(model, indent=2))
        model_file.close()
        
for material in materials_gem :
    for item in items_gem :
        model = {
            "parent": "minecraft:item/generated",
            "textures": {
            "layer0": "omniores:item/%s_%s" % (material, item)
            }
        }
        model_file = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/models/item/' + material + '_' + item + '.json', 'w')
        model_file.write(json.dumps(model, indent=2))
        model_file.close()
        print('Saved ' + material + '_' + item + '.json')
