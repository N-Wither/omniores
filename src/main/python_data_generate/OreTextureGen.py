from PIL import Image

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

ores = [
    "copper",
    # 'silver',
    'redstone',
    'diamond',
    'lapis',
    'emerald',
    'quartz',
    # 'tin',
    # 'lead',
    # 'nickel',
    # 'zinc',
    # 'aluminum',
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

for stone in stones :
    for ore in ores :
        base = Image.open('F:/Creative/diversityMods/omniores/src/main/python_data_generate/assets/minecraft/textures/block/' + stone + '.png').convert('RGBA')
        overlay = Image.open('F:/Creative/diversityMods/omniores/src/main/python_data_generate/assets/omniores/textures/block/overlays/' + ore + '.png').convert('RGBA')
        out = Image.alpha_composite(base, overlay)
        out.save('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/textures/block/' + ore + '_ore_' + stone + '.png')