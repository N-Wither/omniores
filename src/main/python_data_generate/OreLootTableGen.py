import json

stones = [
    # 'stone',
    # 'andesite',
    # 'diorite',
    # 'granite',
    # 'tuff',
    # 'calcite',
    # 'deepslate',
    # 'netherrack',
    # 'blackstone',
    # 'basalt',
    # 'end_stone',
    # 'create_limestone',
    # 'create_scoria',
    # 'create_scorchia',
    # 'quark_jasper',
    'quark_limestone',
    'quark_shale'
]

material = 'silver'
mindrop = 1
maxdrop = 1
item = 'omniores:raw_silver'

ores = [
    '%s_ore_' % (material)
]

loot_table = {
    "type": "minecraft:block",
    "pools": [
    {
      "rolls": 1,
      "bonus_rolls": 0.0,
      "entries": [
        {
          "type": "minecraft:alternatives",
          "children": [
            {
              "type": "minecraft:item",
              "conditions": [
                {
                  "condition": "minecraft:match_tool",
                  "predicate": {
                    "enchantments": [
                      {
                        "enchantment": "minecraft:silk_touch",
                        "levels": {
                          "min": 1
                        }
                      }
                    ]
                  }
                }
              ],
              "name": "omniores:%s_ore_stone" % (material)
            },
            {
              "type": "minecraft:item",
              "functions": [
                {
                  "function": "minecraft:set_count",
                  "count": {
                    "type": "minecraft:uniform",
                    "min": mindrop,
                    "max": maxdrop
                  },
                  "add": False
                },
                {
                  "function": "minecraft:apply_bonus",
                  "enchantment": "minecraft:fortune",
                  "formula": "minecraft:ore_drops"
                },
                {
                  "function": "minecraft:explosion_decay"
                }
              ],
              "name": item
            }
          ]
        }
      ]
    }
  ]
}

for ore in ores :
    for stone in stones :
        print (ore+stone)
        fo = open('F:\Creative\diversityMods\omniores\src\main\\resources\data\omniores\loot_tables\\blocks\\'+ore+stone+'.json', 'w')
        fo.write(json.dumps(loot_table, indent=2))
        fo.close()
