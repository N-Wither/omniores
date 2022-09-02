package net.nwitherkawaii.omniores.utils;

import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.api.distmarker.OnlyIn;
import net.nwitherkawaii.omniores.blocks.BlockRegistry;

public class OmnioresCreativeTab{
    public static CreativeModeTab OMNIORES;

    public static void load(){
        OMNIORES = new CreativeModeTab("omniores") {
            @Override
            public ItemStack makeIcon() {
                return new ItemStack(Item.BY_BLOCK.get(BlockRegistry.IRON_ORE_GRANITE.get()));
            }

            @OnlyIn(Dist.CLIENT)
            public boolean hasSearchBar(){
                return false;
            }
        };
    }
}
