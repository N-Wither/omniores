import json

stones = [
    # "stone",
    # "andesite",
    # "diorite",
    # "granite",
    # "tuff",
    # "calcite",
    # "deepslate",
    # "netherrack",
    # "blackstone",
    # "basalt",
    # "end_stone",
    # 'create_limestone',
    # 'create_scoria',
    # 'create_scorchia',
    'quark_jasper',
    'quark_limestone',
    'quark_shale'
]

ores = [
    # "copper",
    # 'silver',
    # 'redstone',
    # 'diamond',
    # 'lapis',
    # 'emerald',
    # 'quartz',
    # 'tin',
    # 'lead',
    # 'nickel',
    # 'zinc',
    # 'aluminum',
    # 'silver',
    # 'cobalt',
    # 'osmium',
    # 'iridium',
    # 'uranium',
    # 'ruby',
    # 'sapphire',
    # 'sulfur',
    # 'cinnabar',
    # 'potassium_nitrate',
    # 'apatite',
    # 'fluorite',
    'coal',
    'iron',
    'gold'
]


for ore in ores:
    for stone in stones:
        print(ore + "_ore_" + stone)
        model = {
            "parent": "minecraft:block/cube_all",
            "textures": {
                "all": "omniores:block/" + ore + '_ore_' + stone
            }
        }
        block_model_file = open(
            "F:\Creative\diversityMods\omniores\src\main\\resources\\assets\omniores\models\\block\\"
            + ore
            + "_ore_"
            + stone
            + ".json",
            "w",
        )
        block_model_file.write(json.dumps(model, indent=2, separators=(",", ": ")))
        block_model_file.close

        block_state = {
            "variants": {
                "": {
                "model": "omniores:block/" + ore + '_ore_' + stone
                }
            }
        }
        block_state_file = open(
            "F:\Creative\diversityMods\omniores\src\main\\resources\\assets\omniores\\blockstates\\"
            + ore
            + "_ore_"
            + stone
            + '.json',
            'w'
        )
        block_state_file.write(json.dumps(block_state, indent=2, separators=(',', ': ')))
        block_model_file.close()

        item_model = {
            "parent": "omniores:block/" + ore + '_ore_' + stone
        }
        item_model_file = open(
            "F:\Creative\diversityMods\omniores\src\main\\resources\\assets\omniores\models\item\\"
            + ore
            + "_ore_"
            + stone
            + '.json',
            'w'
        )
        item_model_file.write(json.dumps(item_model, indent=2, separators=(',', ': ')))
        item_model_file.close()
