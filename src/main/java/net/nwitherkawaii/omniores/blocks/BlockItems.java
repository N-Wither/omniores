package net.nwitherkawaii.omniores.blocks;

import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.crafting.RecipeType;
import net.minecraft.world.level.block.Block;
import net.nwitherkawaii.omniores.utils.OmnioresCreativeTab;

public class BlockItems extends BlockItem{
    private final int burnTime;

    public BlockItems(Block block, int burnTime) {
        super(block, new Properties().tab(OmnioresCreativeTab.OMNIORES));
        this.burnTime = burnTime;
    }

    @Override
    public int getBurnTime(ItemStack itemStack, RecipeType<?> recipeType) {
        return burnTime;
    }
}
