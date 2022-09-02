import json

stones = [
    "stone",
    "andesite",
    "diorite",
    "granite",
    "tuff",
    "calcite",
    "deepslate",
    "netherrack",
    "blackstone",
    "basalt",
    "end_stone",
    'create_limestone',
    'create_scoria',
    'create_scorchia',
    'quark_jasper',
    'quark_marble',
    'quark_slate'
]

gems = [
    'lapis',
    'diamond',
    'emerald',
    'quartz',
    'ruby',
    'sapphire',
    'redstone'
]

metals = [
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
    'uranium'
]

alloys = [
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

items_metal = [
    'ingot',
    'nugget',
    'plate',
    'dust',
    'gear',
    'rod'
]

items_gem = [
    'dust',
    'gear',
    'plate',
    'rod'
]

chems = [
    'coal',
    'sulfur',
    'cinnabar',
    'potassium_nitrate',
    'apatite',
    'fluorite',
    'coal_coke'
]

lang_EN = {
    "itemGroup.omniores": "OmniOres",
    "item.omniores.charcoal_dust": "Charcoal Dust",
    "item.omniores.obsidian_dust": "Obsidian Dust",
    "item.omniores.wood_dust": "Sawdust",
    "item.omniores.silicon": "Silicon",
    "block.omniores.charcoal_block": "Block of Charcoal"
}

lang_CN = {}

def normalize(str) :
    return str.replace('_', ' ').title()

for gem in gems :
    for stone in stones :
        lang_EN["block.omniores." + gem + '_ore_' + stone] = stone.replace('_', ' ').title() + ' ' + gem.replace('_', ' ').title() + ' Ore'
    lang_EN["block.omniores." + gem + '_block'] = 'Block of ' + gem.replace('_', ' ').title()

for gem in gems :
    for item in items_gem :
        lang_EN['item.omniores.' + gem + '_' + item] = gem.replace('_', ' ').title() + ' ' + item.title()
    lang_EN['item.omniores.' + gem + '_gem'] = normalize(gem)

for chem in chems :
    for stone in stones :
        lang_EN["block.omniores." + chem + '_ore_' + stone] = stone.replace('_', ' ').title() + ' ' + chem.replace('_', ' ').title() + ' Ore'
    lang_EN['block.omniores.' + chem + '_block'] = 'Block of ' + chem.replace('_', ' ').title()
    lang_EN['item.omniores.' + chem + '_dust'] = chem.replace('_', ' ').title() + ' Dust'
    lang_EN['item.omniores.' + chem + '_gem'] = normalize(chem)

for metal in metals :
    for stone in stones :
        lang_EN["block.omniores." + metal + '_ore_' + stone] = normalize(stone) + ' ' + normalize(metal) + ' Ore'
    lang_EN['block.omniores.' + metal + '_block'] = 'Block of ' + normalize(metal)
    lang_EN['item.omniores.raw_' + metal] = 'Raw ' + normalize(metal)
    for item in items_metal :
        lang_EN['item.omniores.' + metal + '_' + item] = normalize(metal) + ' ' + normalize(item)

for alloy in alloys :
    for item in items_metal :
        lang_EN['item.omniores.' + alloy + '_' + item] = normalize(alloy) + ' ' + normalize(item)
    lang_EN['block.omniores.' + alloy + '_block'] = 'Block of ' + normalize(alloy)

file_EN = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/lang/en_us.json', 'w')
file_EN.write(json.dumps(lang_EN, indent=2, sort_keys=True))
file_EN.close()

print('File saved.')
