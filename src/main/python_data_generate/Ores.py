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

ores = [
    "silver"
]

for ore in ores :
    for stone in stones :
        print ('    "omniores:' + ore + '_ore_' + stone + '",')