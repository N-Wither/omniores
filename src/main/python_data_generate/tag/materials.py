import json

template = {
    'replace': False,
    'values': []
}

ingots = {'replace': False, 'values': []}
nuggets = {'replace': False, 'values': []}
dusts = {'replace': False, 'values': []}
plates = {'replace': False, 'values': []}
rods = {'replace': False, 'values': []}
gears = {'replace': False, 'values': []}
raw_materials = {'replace': False, 'values': []}
gems = {'replace': False, 'values': []}


mod_metals = [
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

mod_alloys = [
    'bronze',
    'brass',
    'steel',
    'electrum',
    'invar',
    'constantan',
    'signalum',
    'lumium',
    'enderium'
]

vanilla_metals = ['iron', 'gold']
vanilla_metals_no_nugget = ['copper', 'netherite']

vanilla_gems = ['lapis', 'diamond', 'emerald', 'quartz']
mod_gems = ['ruby', 'sapphire']

chems = ['coal', 'sulfur', 'coal_coke', 'cinnabar', 'potassium_nitrate', 'fluorite', 'apatite']

for material in mod_metals :
    raw_materials['values'].append('omniores:raw_'+material)
    ingots['values'].append('omniores:'+material+'_ingot')
    nuggets['values'].append('omniores:'+material+'_nugget')
    dusts['values'].append('omniores:'+material+'_dust')
    plates['values'].append('omniores:'+material+'_plate')
    rods['values'].append('omniores:'+material+'_rod')
    gears['values'].append('omniores:'+material+'_gear')

    template['values'] = ['omniores:raw_'+material]
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/raw_materials/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_ingot']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ingots/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_nugget']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/nuggets/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_plate']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_rod']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_gear']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

for material in mod_alloys :
    ingots['values'].append('omniores:'+material+'_ingot')
    nuggets['values'].append('omniores:'+material+'_nugget')
    dusts['values'].append('omniores:'+material+'_dust')
    plates['values'].append('omniores:'+material+'_plate')
    rods['values'].append('omniores:'+material+'_rod')
    gears['values'].append('omniores:'+material+'_gear')

    template['values'] = ['omniores:'+material+'_ingot']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ingots/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_nugget']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/nuggets/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_plate']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_rod']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_gear']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

for material in vanilla_metals :
    dusts['values'].append('omniores:'+material+'_dust')
    plates['values'].append('omniores:'+material+'_plate')
    rods['values'].append('omniores:'+material+'_rod')
    gears['values'].append('omniores:'+material+'_gear')

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_plate']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_rod']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_gear']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

for material in vanilla_metals_no_nugget :
    nuggets['values'].append('omniores:'+material+'_nugget')
    dusts['values'].append('omniores:'+material+'_dust')
    plates['values'].append('omniores:'+material+'_plate')
    rods['values'].append('omniores:'+material+'_rod')
    gears['values'].append('omniores:'+material+'_gear')

    template['values'] = ['omniores:'+material+'_nugget']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/nuggets/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_plate']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_rod']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_gear']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

for material in vanilla_gems :
    dusts['values'].append('omniores:'+material+'_dust')
    plates['values'].append('omniores:'+material+'_plate')
    rods['values'].append('omniores:'+material+'_rod')
    gears['values'].append('omniores:'+material+'_gear')

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_plate']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_rod']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_gear']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

for material in mod_gems :
    gems['values'].append('omniores:'+material+'_gem')
    dusts['values'].append('omniores:'+material+'_dust')
    plates['values'].append('omniores:'+material+'_plate')
    rods['values'].append('omniores:'+material+'_rod')
    gears['values'].append('omniores:'+material+'_gear')

    template['values'] = ['omniores:'+material+'_gem']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gems/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_plate']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_rod']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_gear']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

for material in chems :
    gems['values'].append('omniores:'+material+'_gem')
    dusts['values'].append('omniores:'+material+'_dust')

    template['values'] = ['omniores:'+material+'_gem']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gems/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

    template['values'] = ['omniores:'+material+'_dust']
    file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts/%s.json' % (material), 'w')
    file.write(json.dumps(template, indent=2))
    file.close()

def putJson(replace, content, path, file_name,):
    temp = {"replace": False, "values": []}
    if replace == True :
        temp['values'] = [content]
        file = open(path + file_name + '.json', 'w')
        file.write(json.dumps(temp, indent=2))
        file.close()
    else :
        temp['values'].append(content)
        file = open(path + file_name + '.json', 'w')
        file.write(json.dumps(temp, indent=2))
        file.close()
    print('File saved: '+file_name+'.json')

# Misc
dusts['values'].append('omniores:obsidian_dust')
dusts['values'].append('omniores:charcoal_dust')
dusts['values'].append('omniores:wood_dust')
gems['values'].append('omniores:silicon')

putJson(0, 'omniores:silicon_gem', 'F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/', 'silicon')
putJson(0, 'omniores:silicon_gem', 'F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gems/', 'silicon')

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/raw_materials.json', 'w')
file.write(json.dumps(raw_materials, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/ingots.json', 'w')
file.write(json.dumps(ingots, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/nuggets.json', 'w')
file.write(json.dumps(nuggets, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/dusts.json', 'w')
file.write(json.dumps(dusts, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/plates.json', 'w')
file.write(json.dumps(plates, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gears.json', 'w')
file.write(json.dumps(gears, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/rods.json', 'w')
file.write(json.dumps(rods, indent=2))
file.close()

file = open('F:/Creative/diversityMods/omniores/src/main/resources/data/forge/tags/items/gems.json', 'w')
file.write(json.dumps(gems, indent=2))
file.close()
