materials_metal = [
    'iron',
    # 'copper',
    # 'gold',
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
    # 'bronze',
    # 'brass',
    # 'steel',
    # 'electrum',
    # 'invar',
    # 'constantan',
    # 'signalum',
    # 'lumium',
    # 'enderium',
    # 'netherite',
]

materials_gem = [
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
    'coal_coke'
]

for material in materials_metal :
    print('    // %s' % (material))
    print('    public static final RegistryObject<Item> RAW_%s = ITEMS.register("raw_%s", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_INGOT = ITEMS.register("%s_ingot", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_NUGGET = ITEMS.register("%s_nugget", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_DUST = ITEMS.register("%s_dust", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_PLATE = ITEMS.register("%s_plate", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_ROD = ITEMS.register("%s_rod", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_GEAR = ITEMS.register("%s_gear", ItemProperties::new);\n' % (material.upper(), material))

for material in materials_gem:
    print('    // %s' % (material))
    print('    public static final RegistryObject<Item> %s_GEM = ITEMS.register("%s_gem", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_DUST = ITEMS.register("%s_dust", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_PLATE = ITEMS.register("%s_plate", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_ROD = ITEMS.register("%s_rod", ItemProperties::new);' % (material.upper(), material))
    print('    public static final RegistryObject<Item> %s_GEAR = ITEMS.register("%s_gear", ItemProperties::new);\n' % (material.upper(), material))