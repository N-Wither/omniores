package net.nwitherkawaii.omniores;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.RegistryEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.InterModComms;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.event.lifecycle.InterModEnqueueEvent;
import net.minecraftforge.fml.event.lifecycle.InterModProcessEvent;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.nwitherkawaii.omniores.blocks.BlockRegistry;
import net.nwitherkawaii.omniores.items.BlockItemRegistry;
import net.nwitherkawaii.omniores.items.ItemRegistry;
import net.nwitherkawaii.omniores.utils.OmnioresCreativeTab;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.stream.Collectors;

// The value here should match an entry in the META-INF/mods.toml file
@Mod("omniores")
public class OmnioresMod
{
    public static final String MOD_ID = "omniores";

    // Directly reference a log4j logger
    public static final Logger LOGGER =  LogManager.getLogger(MOD_ID);

    public OmnioresMod()
    {
        final IEventBus FML = FMLJavaModLoadingContext.get().getModEventBus();
        final IEventBus MTA = MinecraftForge.EVENT_BUS;

        // Register the setup method for modloading
        FML.addListener(this::setup);

        // Register ourselves for server and other game events we are interested in
        MTA.register(this);

        OmnioresCreativeTab.load();
        ItemRegistry.ITEMS.register(FML);
        BlockItemRegistry.ITEMS.register(FML);
        BlockRegistry.BLOCKS.register(FML);
    }

    private void setup(final FMLCommonSetupEvent event)
    {
        // some preinit code
        LOGGER.info("[OmniOres] OmniOres is loading!");
    }

    // You can use SubscribeEvent and let the Event Bus discover methods to call
    @SubscribeEvent
    public void onServerStarting(ServerStartingEvent event)
    {
        // Do something when the server starts
        LOGGER.info("[OmniOres] OmniOres is on server!");
    }

    // You can use EventBusSubscriber to automatically subscribe events on the contained class (this is subscribing to the MOD
    // Event bus for receiving Registry Events)
    @Mod.EventBusSubscriber(bus = Mod.EventBusSubscriber.Bus.MOD)
    public static class RegistryEvents
    {
        @SubscribeEvent
        public static void onBlocksRegistry(final RegistryEvent.Register<Block> blockRegistryEvent)
        {
            // Register a new block here
            LOGGER.info("[OmniOres] OmniOres is registering blocks!");
        }
    }
}
