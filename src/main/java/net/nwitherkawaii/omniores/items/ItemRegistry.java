package net.nwitherkawaii.omniores.items;

import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.nwitherkawaii.omniores.OmnioresMod;

import net.minecraft.world.item.Item;

public class ItemRegistry {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, OmnioresMod.MOD_ID);

    // iron
    public static final RegistryObject<Item> IRON_DUST = ITEMS.register("iron_dust", BasicItems::new);
    public static final RegistryObject<Item> IRON_PLATE = ITEMS.register("iron_plate", BasicItems::new);
    public static final RegistryObject<Item> IRON_ROD = ITEMS.register("iron_rod", BasicItems::new);
    public static final RegistryObject<Item> IRON_GEAR = ITEMS.register("iron_gear", BasicItems::new);

    // copper
    public static final RegistryObject<Item> COPPER_NUGGET = ITEMS.register("copper_nugget", BasicItems::new);
    public static final RegistryObject<Item> COPPER_DUST = ITEMS.register("copper_dust", BasicItems::new);
    public static final RegistryObject<Item> COPPER_PLATE = ITEMS.register("copper_plate", BasicItems::new);
    public static final RegistryObject<Item> COPPER_ROD = ITEMS.register("copper_rod", BasicItems::new);
    public static final RegistryObject<Item> COPPER_GEAR = ITEMS.register("copper_gear", BasicItems::new);

    // gold
    public static final RegistryObject<Item> GOLD_DUST = ITEMS.register("gold_dust", BasicItems::new);
    public static final RegistryObject<Item> GOLD_PLATE = ITEMS.register("gold_plate", BasicItems::new);
    public static final RegistryObject<Item> GOLD_ROD = ITEMS.register("gold_rod", BasicItems::new);
    public static final RegistryObject<Item> GOLD_GEAR = ITEMS.register("gold_gear", BasicItems::new);

    // tin
    public static final RegistryObject<Item> RAW_TIN = ITEMS.register("raw_tin", BasicItems::new);
    public static final RegistryObject<Item> TIN_INGOT = ITEMS.register("tin_ingot", BasicItems::new);
    public static final RegistryObject<Item> TIN_NUGGET = ITEMS.register("tin_nugget", BasicItems::new);
    public static final RegistryObject<Item> TIN_DUST = ITEMS.register("tin_dust", BasicItems::new);
    public static final RegistryObject<Item> TIN_PLATE = ITEMS.register("tin_plate", BasicItems::new);
    public static final RegistryObject<Item> TIN_ROD = ITEMS.register("tin_rod", BasicItems::new);
    public static final RegistryObject<Item> TIN_GEAR = ITEMS.register("tin_gear", BasicItems::new);

    // lead
    public static final RegistryObject<Item> RAW_LEAD = ITEMS.register("raw_lead", BasicItems::new);
    public static final RegistryObject<Item> LEAD_INGOT = ITEMS.register("lead_ingot", BasicItems::new);
    public static final RegistryObject<Item> LEAD_NUGGET = ITEMS.register("lead_nugget", BasicItems::new);
    public static final RegistryObject<Item> LEAD_DUST = ITEMS.register("lead_dust", BasicItems::new);
    public static final RegistryObject<Item> LEAD_PLATE = ITEMS.register("lead_plate", BasicItems::new);
    public static final RegistryObject<Item> LEAD_ROD = ITEMS.register("lead_rod", BasicItems::new);
    public static final RegistryObject<Item> LEAD_GEAR = ITEMS.register("lead_gear", BasicItems::new);

    // nickel
    public static final RegistryObject<Item> RAW_NICKEL = ITEMS.register("raw_nickel", BasicItems::new);
    public static final RegistryObject<Item> NICKEL_INGOT = ITEMS.register("nickel_ingot", BasicItems::new);
    public static final RegistryObject<Item> NICKEL_NUGGET = ITEMS.register("nickel_nugget", BasicItems::new);
    public static final RegistryObject<Item> NICKEL_DUST = ITEMS.register("nickel_dust", BasicItems::new);
    public static final RegistryObject<Item> NICKEL_PLATE = ITEMS.register("nickel_plate", BasicItems::new);
    public static final RegistryObject<Item> NICKEL_ROD = ITEMS.register("nickel_rod", BasicItems::new);
    public static final RegistryObject<Item> NICKEL_GEAR = ITEMS.register("nickel_gear", BasicItems::new);

    // zinc
    public static final RegistryObject<Item> RAW_ZINC = ITEMS.register("raw_zinc", BasicItems::new);
    public static final RegistryObject<Item> ZINC_INGOT = ITEMS.register("zinc_ingot", BasicItems::new);
    public static final RegistryObject<Item> ZINC_NUGGET = ITEMS.register("zinc_nugget", BasicItems::new);
    public static final RegistryObject<Item> ZINC_DUST = ITEMS.register("zinc_dust", BasicItems::new);
    public static final RegistryObject<Item> ZINC_PLATE = ITEMS.register("zinc_plate", BasicItems::new);
    public static final RegistryObject<Item> ZINC_ROD = ITEMS.register("zinc_rod", BasicItems::new);
    public static final RegistryObject<Item> ZINC_GEAR = ITEMS.register("zinc_gear", BasicItems::new);

    // aluminum
    public static final RegistryObject<Item> RAW_ALUMINUM = ITEMS.register("raw_aluminum", BasicItems::new);
    public static final RegistryObject<Item> ALUMINUM_INGOT = ITEMS.register("aluminum_ingot", BasicItems::new);
    public static final RegistryObject<Item> ALUMINUM_NUGGET = ITEMS.register("aluminum_nugget", BasicItems::new);
    public static final RegistryObject<Item> ALUMINUM_DUST = ITEMS.register("aluminum_dust", BasicItems::new);
    public static final RegistryObject<Item> ALUMINUM_PLATE = ITEMS.register("aluminum_plate", BasicItems::new);
    public static final RegistryObject<Item> ALUMINUM_ROD = ITEMS.register("aluminum_rod", BasicItems::new);
    public static final RegistryObject<Item> ALUMINUM_GEAR = ITEMS.register("aluminum_gear", BasicItems::new);

    // silver
    public static final RegistryObject<Item> RAW_SILVER = ITEMS.register("raw_silver", BasicItems::new);
    public static final RegistryObject<Item> SILVER_INGOT = ITEMS.register("silver_ingot", BasicItems::new);
    public static final RegistryObject<Item> SILVER_NUGGET = ITEMS.register("silver_nugget", BasicItems::new);
    public static final RegistryObject<Item> SILVER_DUST = ITEMS.register("silver_dust", BasicItems::new);
    public static final RegistryObject<Item> SILVER_PLATE = ITEMS.register("silver_plate", BasicItems::new);
    public static final RegistryObject<Item> SILVER_ROD = ITEMS.register("silver_rod", BasicItems::new);
    public static final RegistryObject<Item> SILVER_GEAR = ITEMS.register("silver_gear", BasicItems::new);

    // cobalt
    public static final RegistryObject<Item> RAW_COBALT = ITEMS.register("raw_cobalt", BasicItems::new);
    public static final RegistryObject<Item> COBALT_INGOT = ITEMS.register("cobalt_ingot", BasicItems::new);
    public static final RegistryObject<Item> COBALT_NUGGET = ITEMS.register("cobalt_nugget", BasicItems::new);
    public static final RegistryObject<Item> COBALT_DUST = ITEMS.register("cobalt_dust", BasicItems::new);
    public static final RegistryObject<Item> COBALT_PLATE = ITEMS.register("cobalt_plate", BasicItems::new);
    public static final RegistryObject<Item> COBALT_ROD = ITEMS.register("cobalt_rod", BasicItems::new);
    public static final RegistryObject<Item> COBALT_GEAR = ITEMS.register("cobalt_gear", BasicItems::new);

    // osmium
    public static final RegistryObject<Item> RAW_OSMIUM = ITEMS.register("raw_osmium", BasicItems::new);
    public static final RegistryObject<Item> OSMIUM_INGOT = ITEMS.register("osmium_ingot", BasicItems::new);
    public static final RegistryObject<Item> OSMIUM_NUGGET = ITEMS.register("osmium_nugget", BasicItems::new);
    public static final RegistryObject<Item> OSMIUM_DUST = ITEMS.register("osmium_dust", BasicItems::new);
    public static final RegistryObject<Item> OSMIUM_PLATE = ITEMS.register("osmium_plate", BasicItems::new);
    public static final RegistryObject<Item> OSMIUM_ROD = ITEMS.register("osmium_rod", BasicItems::new);
    public static final RegistryObject<Item> OSMIUM_GEAR = ITEMS.register("osmium_gear", BasicItems::new);

    // iridium
    public static final RegistryObject<Item> RAW_IRIDIUM = ITEMS.register("raw_iridium", BasicItems::new);
    public static final RegistryObject<Item> IRIDIUM_INGOT = ITEMS.register("iridium_ingot", BasicItems::new);
    public static final RegistryObject<Item> IRIDIUM_NUGGET = ITEMS.register("iridium_nugget", BasicItems::new);
    public static final RegistryObject<Item> IRIDIUM_DUST = ITEMS.register("iridium_dust", BasicItems::new);
    public static final RegistryObject<Item> IRIDIUM_PLATE = ITEMS.register("iridium_plate", BasicItems::new);
    public static final RegistryObject<Item> IRIDIUM_ROD = ITEMS.register("iridium_rod", BasicItems::new);
    public static final RegistryObject<Item> IRIDIUM_GEAR = ITEMS.register("iridium_gear", BasicItems::new);

    // uranium
    public static final RegistryObject<Item> RAW_URANIUM = ITEMS.register("raw_uranium", BasicItems::new);
    public static final RegistryObject<Item> URANIUM_INGOT = ITEMS.register("uranium_ingot", BasicItems::new);
    public static final RegistryObject<Item> URANIUM_NUGGET = ITEMS.register("uranium_nugget", BasicItems::new);
    public static final RegistryObject<Item> URANIUM_DUST = ITEMS.register("uranium_dust", BasicItems::new);
    public static final RegistryObject<Item> URANIUM_PLATE = ITEMS.register("uranium_plate", BasicItems::new);
    public static final RegistryObject<Item> URANIUM_ROD = ITEMS.register("uranium_rod", BasicItems::new);
    public static final RegistryObject<Item> URANIUM_GEAR = ITEMS.register("uranium_gear", BasicItems::new);

    // bronze
    public static final RegistryObject<Item> BRONZE_INGOT = ITEMS.register("bronze_ingot", BasicItems::new);
    public static final RegistryObject<Item> BRONZE_NUGGET = ITEMS.register("bronze_nugget", BasicItems::new);
    public static final RegistryObject<Item> BRONZE_DUST = ITEMS.register("bronze_dust", BasicItems::new);
    public static final RegistryObject<Item> BRONZE_PLATE = ITEMS.register("bronze_plate", BasicItems::new);
    public static final RegistryObject<Item> BRONZE_ROD = ITEMS.register("bronze_rod", BasicItems::new);
    public static final RegistryObject<Item> BRONZE_GEAR = ITEMS.register("bronze_gear", BasicItems::new);

    // brass
    public static final RegistryObject<Item> BRASS_INGOT = ITEMS.register("brass_ingot", BasicItems::new);
    public static final RegistryObject<Item> BRASS_NUGGET = ITEMS.register("brass_nugget", BasicItems::new);
    public static final RegistryObject<Item> BRASS_DUST = ITEMS.register("brass_dust", BasicItems::new);
    public static final RegistryObject<Item> BRASS_PLATE = ITEMS.register("brass_plate", BasicItems::new);
    public static final RegistryObject<Item> BRASS_ROD = ITEMS.register("brass_rod", BasicItems::new);
    public static final RegistryObject<Item> BRASS_GEAR = ITEMS.register("brass_gear", BasicItems::new);

    // steel
    public static final RegistryObject<Item> STEEL_INGOT = ITEMS.register("steel_ingot", BasicItems::new);
    public static final RegistryObject<Item> STEEL_NUGGET = ITEMS.register("steel_nugget", BasicItems::new);
    public static final RegistryObject<Item> STEEL_DUST = ITEMS.register("steel_dust", BasicItems::new);
    public static final RegistryObject<Item> STEEL_PLATE = ITEMS.register("steel_plate", BasicItems::new);
    public static final RegistryObject<Item> STEEL_ROD = ITEMS.register("steel_rod", BasicItems::new);
    public static final RegistryObject<Item> STEEL_GEAR = ITEMS.register("steel_gear", BasicItems::new);

    // electrum
    public static final RegistryObject<Item> ELECTRUM_INGOT = ITEMS.register("electrum_ingot", BasicItems::new);
    public static final RegistryObject<Item> ELECTRUM_NUGGET = ITEMS.register("electrum_nugget", BasicItems::new);
    public static final RegistryObject<Item> ELECTRUM_DUST = ITEMS.register("electrum_dust", BasicItems::new);
    public static final RegistryObject<Item> ELECTRUM_PLATE = ITEMS.register("electrum_plate", BasicItems::new);
    public static final RegistryObject<Item> ELECTRUM_ROD = ITEMS.register("electrum_rod", BasicItems::new);
    public static final RegistryObject<Item> ELECTRUM_GEAR = ITEMS.register("electrum_gear", BasicItems::new);

    // invar
    public static final RegistryObject<Item> INVAR_INGOT = ITEMS.register("invar_ingot", BasicItems::new);
    public static final RegistryObject<Item> INVAR_NUGGET = ITEMS.register("invar_nugget", BasicItems::new);
    public static final RegistryObject<Item> INVAR_DUST = ITEMS.register("invar_dust", BasicItems::new);
    public static final RegistryObject<Item> INVAR_PLATE = ITEMS.register("invar_plate", BasicItems::new);
    public static final RegistryObject<Item> INVAR_ROD = ITEMS.register("invar_rod", BasicItems::new);
    public static final RegistryObject<Item> INVAR_GEAR = ITEMS.register("invar_gear", BasicItems::new);

    // constantan
    public static final RegistryObject<Item> CONSTANTAN_INGOT = ITEMS.register("constantan_ingot", BasicItems::new);
    public static final RegistryObject<Item> CONSTANTAN_NUGGET = ITEMS.register("constantan_nugget", BasicItems::new);
    public static final RegistryObject<Item> CONSTANTAN_DUST = ITEMS.register("constantan_dust", BasicItems::new);
    public static final RegistryObject<Item> CONSTANTAN_PLATE = ITEMS.register("constantan_plate", BasicItems::new);
    public static final RegistryObject<Item> CONSTANTAN_ROD = ITEMS.register("constantan_rod", BasicItems::new);
    public static final RegistryObject<Item> CONSTANTAN_GEAR = ITEMS.register("constantan_gear", BasicItems::new);

    // signalum
    public static final RegistryObject<Item> SIGNALUM_INGOT = ITEMS.register("signalum_ingot", BasicItems::new);
    public static final RegistryObject<Item> SIGNALUM_NUGGET = ITEMS.register("signalum_nugget", BasicItems::new);
    public static final RegistryObject<Item> SIGNALUM_DUST = ITEMS.register("signalum_dust", BasicItems::new);
    public static final RegistryObject<Item> SIGNALUM_PLATE = ITEMS.register("signalum_plate", BasicItems::new);
    public static final RegistryObject<Item> SIGNALUM_ROD = ITEMS.register("signalum_rod", BasicItems::new);
    public static final RegistryObject<Item> SIGNALUM_GEAR = ITEMS.register("signalum_gear", BasicItems::new);

    // lumium
    public static final RegistryObject<Item> LUMIUM_INGOT = ITEMS.register("lumium_ingot", BasicItems::new);
    public static final RegistryObject<Item> LUMIUM_NUGGET = ITEMS.register("lumium_nugget", BasicItems::new);
    public static final RegistryObject<Item> LUMIUM_DUST = ITEMS.register("lumium_dust", BasicItems::new);
    public static final RegistryObject<Item> LUMIUM_PLATE = ITEMS.register("lumium_plate", BasicItems::new);
    public static final RegistryObject<Item> LUMIUM_ROD = ITEMS.register("lumium_rod", BasicItems::new);
    public static final RegistryObject<Item> LUMIUM_GEAR = ITEMS.register("lumium_gear", BasicItems::new);

    // enderium
    public static final RegistryObject<Item> ENDERIUM_INGOT = ITEMS.register("enderium_ingot", BasicItems::new);
    public static final RegistryObject<Item> ENDERIUM_NUGGET = ITEMS.register("enderium_nugget", BasicItems::new);
    public static final RegistryObject<Item> ENDERIUM_DUST = ITEMS.register("enderium_dust", BasicItems::new);
    public static final RegistryObject<Item> ENDERIUM_PLATE = ITEMS.register("enderium_plate", BasicItems::new);
    public static final RegistryObject<Item> ENDERIUM_ROD = ITEMS.register("enderium_rod", BasicItems::new);
    public static final RegistryObject<Item> ENDERIUM_GEAR = ITEMS.register("enderium_gear", BasicItems::new);

    // netherite
    public static final RegistryObject<Item> NETHERITE_NUGGET = ITEMS.register("netherite_nugget", BasicItems::new);
    public static final RegistryObject<Item> NETHERITE_DUST = ITEMS.register("netherite_dust", BasicItems::new);
    public static final RegistryObject<Item> NETHERITE_PLATE = ITEMS.register("netherite_plate", BasicItems::new);
    public static final RegistryObject<Item> NETHERITE_ROD = ITEMS.register("netherite_rod", BasicItems::new);
    public static final RegistryObject<Item> NETHERITE_GEAR = ITEMS.register("netherite_gear", BasicItems::new);

    // lapis
    public static final RegistryObject<Item> LAPIS_DUST = ITEMS.register("lapis_dust", BasicItems::new);
    public static final RegistryObject<Item> LAPIS_PLATE = ITEMS.register("lapis_plate", BasicItems::new);
    public static final RegistryObject<Item> LAPIS_ROD = ITEMS.register("lapis_rod", BasicItems::new);
    public static final RegistryObject<Item> LAPIS_GEAR = ITEMS.register("lapis_gear", BasicItems::new);

    // diamond
    public static final RegistryObject<Item> DIAMOND_DUST = ITEMS.register("diamond_dust", BasicItems::new);
    public static final RegistryObject<Item> DIAMOND_PLATE = ITEMS.register("diamond_plate", BasicItems::new);
    public static final RegistryObject<Item> DIAMOND_ROD = ITEMS.register("diamond_rod", BasicItems::new);
    public static final RegistryObject<Item> DIAMOND_GEAR = ITEMS.register("diamond_gear", BasicItems::new);

    // emerald
    public static final RegistryObject<Item> EMERALD_DUST = ITEMS.register("emerald_dust", BasicItems::new);
    public static final RegistryObject<Item> EMERALD_PLATE = ITEMS.register("emerald_plate", BasicItems::new);
    public static final RegistryObject<Item> EMERALD_ROD = ITEMS.register("emerald_rod", BasicItems::new);
    public static final RegistryObject<Item> EMERALD_GEAR = ITEMS.register("emerald_gear", BasicItems::new);

    // ruby
    public static final RegistryObject<Item> RUBY_GEM = ITEMS.register("ruby_gem", BasicItems::new);
    public static final RegistryObject<Item> RUBY_DUST = ITEMS.register("ruby_dust", BasicItems::new);
    public static final RegistryObject<Item> RUBY_PLATE = ITEMS.register("ruby_plate", BasicItems::new);
    public static final RegistryObject<Item> RUBY_ROD = ITEMS.register("ruby_rod", BasicItems::new);
    public static final RegistryObject<Item> RUBY_GEAR = ITEMS.register("ruby_gear", BasicItems::new);

    // sapphire
    public static final RegistryObject<Item> SAPPHIRE_GEM = ITEMS.register("sapphire_gem", BasicItems::new);
    public static final RegistryObject<Item> SAPPHIRE_DUST = ITEMS.register("sapphire_dust", BasicItems::new);
    public static final RegistryObject<Item> SAPPHIRE_PLATE = ITEMS.register("sapphire_plate", BasicItems::new);
    public static final RegistryObject<Item> SAPPHIRE_ROD = ITEMS.register("sapphire_rod", BasicItems::new);
    public static final RegistryObject<Item> SAPPHIRE_GEAR = ITEMS.register("sapphire_gear", BasicItems::new);

    // coal_coke
    public static final RegistryObject<Item> COAL_COKE_GEM = ITEMS.register("coal_coke_gem", () -> new BurnableItems(3200));
    public static final RegistryObject<Item> COAL_COKE_DUST = ITEMS.register("coal_coke_dust", () -> new BurnableItems(3200));

    // coal
    public static final RegistryObject<Item> COAL_DUST = ITEMS.register("coal_dust", () -> new BurnableItems(1600));

    // sulfur
    public static final RegistryObject<Item> SULFUR_GEM = ITEMS.register("sulfur_gem", () -> new BurnableItems(1200));
    public static final RegistryObject<Item> SULFUR_DUST = ITEMS.register("sulfur_dust", () -> new BurnableItems(1200));

    // cinnabar
    public static final RegistryObject<Item> CINNABAR_GEM = ITEMS.register("cinnabar_gem", BasicItems::new);
    public static final RegistryObject<Item> CINNABAR_DUST = ITEMS.register("cinnabar_dust", BasicItems::new);

    // potassium_nitrate
    public static final RegistryObject<Item> POTASSIUM_NITRATE_GEM = ITEMS.register("potassium_nitrate_gem", BasicItems::new);
    public static final RegistryObject<Item> POTASSIUM_NITRATE_DUST = ITEMS.register("potassium_nitrate_dust", BasicItems::new);

    // apatite
    public static final RegistryObject<Item> APATITE_GEM = ITEMS.register("apatite_gem", BasicItems::new);
    public static final RegistryObject<Item> APATITE_DUST = ITEMS.register("apatite_dust", BasicItems::new);

    // fluorite
    public static final RegistryObject<Item> FLUORITE_GEM = ITEMS.register("fluorite_gem", BasicItems::new);
    public static final RegistryObject<Item> FLUORITE_DUST = ITEMS.register("fluorite_dust", BasicItems::new);

    // quartz
    public static final RegistryObject<Item> QUARTZ_DUST = ITEMS.register("quartz_dust", BasicItems::new);
    public static final RegistryObject<Item> QUARTZ_GEAR = ITEMS.register("quartz_gear", BasicItems::new);

    // Misc
    public static final RegistryObject<Item> CHARCOAL_DUST = ITEMS.register("charcoal_dust", () -> new BurnableItems(1600));
    public static final RegistryObject<Item> OBSIDIAN_DUST = ITEMS.register("obsidian_dust", BasicItems::new);
    public static final RegistryObject<Item> WOOD_DUST = ITEMS.register("wood_dust", () -> new BurnableItems(100));
    public static final RegistryObject<Item> SILICON = ITEMS.register("silicon", BasicItems::new);
    public static final RegistryObject<Item> ENDER_DUST = ITEMS.register("ender_dust", BasicItems::new);

}
