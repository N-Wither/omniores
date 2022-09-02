import json

materials = [
    "tin",
    "lead",
    "nickel",
    "zinc",
    "aluminum",
    "silver",
    "cobalt",
    "osmium",
    "iridium",
    "uranium",
    "bronze",
    "brass",
    "steel",
    "electrum",
    "invar",
    "constantan",
    "signalum",
    "lumium",
    "enderium",
    "ruby",
    "sapphire",
    "sulfur",
    "cinnabar",
    "potassium_nitrate",
    "apatite",
    "fluorite",
    "coal_coke",
    "charcoal"
]

storages = {
    'replace': False,
    'values': []
}

storages_specific = {
    'replace': False,
    'values': []
}

for material in materials :
    storages["values"].append('omniores:'+material+'_block')
    storages_specific["values"].append('omniores:'+material+'_block')
    storages_specific_file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/storage_blocks/%s.json' % (material), 'w')
    storages_specific_file.write(json.dumps(storages_specific, indent=2))
    storages_specific["values"] = []

storages_file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/storage_blocks.json', 'w')
storages_file.write(json.dumps(storages, indent=2))
