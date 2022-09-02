package net.nwitherkawaii.omniores.items;

import net.minecraft.world.item.Item;
import net.nwitherkawaii.omniores.utils.OmnioresCreativeTab;

public class BasicItems extends Item{
    public BasicItems(){
        super(new Item.Properties().tab(OmnioresCreativeTab.OMNIORES));
    }
}