import json
from textwrap import indent

materials = [
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
    'netherite',
    'lapis',
    'diamond',
    'emerald',
    'ruby',
    'sapphire',
    'coal',
    'sulfur',
    'cinnabar',
    'potassium_nitrate',
    'apatite',
    'fluorite',
    'coal_coke',
    'charcoal'
]

for material in materials :
    # print('    public static final RegistryObject<Block> %s_BLOCK = BLOCKS.register("%s_block", () -> new Block(STORAGE_BLOCK));' % (material.upper(), material))
    pass

print('')

for material in materials :
    # print('    public static final RegistryObject<Item> %s_BLOCK = ITEMS.register("%s_block", () -> new BlockItem(BlockRegistry.%s_BLOCK.get(), new Item.Properties().tab(OmnioresCreativeTab.OMNIORES)));' % (material.upper(), material, material.upper()))
    pass

for material in materials :
    # Block Model
    block_model = {
        "parent": "minecraft:block/cube_all",
        "textures": {
            "all": "omniores:block/" + material + '_block'
        }
    }
    block_model_file = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/models/block/' + material + '_block.json', 'w')
    block_model_file.write(json.dumps(block_model, indent=2))
    block_model_file.close()
    print('Saved models/block/' + material + '_block.json')

    # Block State
    block_state = {
        "variants": {
            "": {
            "model": "omniores:block/" + material + '_block'
            }
        }
    }
    block_state_file = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/blockstates/' + material + '_block.json', 'w')
    block_state_file.write(json.dumps(block_state, indent=2))
    block_state_file.close()
    print('Saved blockstates/' + material + '_block.json')

    # Item Model
    item_model = {"parent":"omniores:block/" + material + '_block'}
    item_model_file = open('F:/Creative/diversityMods/omniores/src/main/resources/assets/omniores/models/item/' + material + '_block.json', 'w')
    item_model_file.write(json.dumps(item_model))
    item_model_file.close()
    print('Saved models/item/' + material)