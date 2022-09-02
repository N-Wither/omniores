package net.nwitherkawaii.omniores.items;

import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.crafting.RecipeType;
import net.nwitherkawaii.omniores.utils.OmnioresCreativeTab;

public class BurnableItems extends Item{
    private final int burnTime;

    public BurnableItems(int burnTime) {
        super(new Properties().tab(OmnioresCreativeTab.OMNIORES));
        this.burnTime = burnTime;
    }

    @Override
    public int getBurnTime(ItemStack itemStack, RecipeType<?> recipeType) {
        return burnTime;
    }
}
