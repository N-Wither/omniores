ov_stones = [
    "stone",
    "andesite",
    "diorite",
    "granite",
    "tuff",
    "calcite",
    'create_limestone',
    'create_scoria',
    'create_scorchia',
    'quark_jasper',
    'quark_marble',
    'quark_slate'
]
ov_stones.sort()

ne_stones = [
    'netherrack',
    'blackstone',
    'basalt'
]
ne_stones.sort()

ed_stones = [
    'end_stone'
]
ed_stones.sort()

material = 'silver'

expmax = 0
expmin = 0

# Functions
def ore_register(ore, expmin, expmax, stone) :
    return '    public static final RegistryObject<OreBlocks> %s_ORE_%s = BLOCKS.register("%s_ore_%s", () -> new OreBlocks(OVERWORLD_ORES, UniformInt.of(%d, %d)));' % (
        ore.upper(), stone.upper(), ore, stone, expmin, expmax
    )

def ore_item_register(ore, stone) :
    return '    public static final RegistryObject<Item> %s_ORE_%s = ITEMS.register("%s_ore_%s", () -> new BlockItem(BlockRegistry.%s_ORE_%s.get(), new Item.Properties().tab(OmnioresCreativeTab.OMNIORES)));' % (
        ore.upper(), stone.upper(), ore, stone, ore.upper(), stone.upper()
    )

# BlockRegistry
for stone in ov_stones :
    print( ore_register(material, expmin, expmax, stone) )

print ('    public static final RegistryObject<OreBlocks> %s_ORE_DEEPSLATE = BLOCKS.register("%s_ore_deepslate", () -> new OreBlocks(OVERWORLD_ORES_HARD, UniformInt.of(%d, %d)));' % (
    material.upper(), material, expmin, expmax
))

for stone in ne_stones :
    print('    public static final RegistryObject<OreBlocks> %s_ORE_%s = BLOCKS.register("%s_ore_%s", () -> new OreBlocks(NETHER_ORES, UniformInt.of(%d, %d)));' % (
        material.upper(), stone.upper(), material, stone, expmin, expmax
    ))

for stone in ed_stones :
    print('    public static final RegistryObject<OreBlocks> %s_ORE_%s = BLOCKS.register("%s_ore_%s", () -> new OreBlocks(END_ORES, UniformInt.of(%d, %d)));' % (
        material.upper(), stone.upper(), material, stone, expmin, expmax
    ))

# BlockItemRegistry
print ('\n And here is BlockItems :')

for stone in ov_stones :
    print( ore_item_register(material, stone) )

print ('    public static final RegistryObject<Item> %s_ORE_DEEPSLATE = ITEMS.register("%s_ore_deepslate", () -> new BlockItem(BlockRegistry.%s_ORE_DEEPSLATE.get(), new Item.Properties().tab(OmnioresCreativeTab.OMNIORES)));' % (
    material.upper(), material, material.upper()
))

for stone in ne_stones :
    print('    public static final RegistryObject<Item> %s_ORE_%s = ITEMS.register("%s_ore_%s", () -> new BlockItem(BlockRegistry.%s_ORE_%s.get(), new Item.Properties().tab(OmnioresCreativeTab.OMNIORES)));' % (
        material.upper(), stone.upper(), material, stone, material.upper(), stone.upper()
    ))

for stone in ed_stones :
    print('    public static final RegistryObject<Item> %s_ORE_%s = ITEMS.register("%s_ore_%s", () -> new BlockItem(BlockRegistry.%s_ORE_%s.get(), new Item.Properties().tab(OmnioresCreativeTab.OMNIORES)));' % (
        material.upper(), stone.upper(), material, stone, material.upper(), stone.upper()
    ))