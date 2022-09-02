package net.nwitherkawaii.omniores.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.util.valueproviders.UniformInt;
import net.minecraft.world.entity.ExperienceOrb;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Explosion;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.LevelAccessor;
import net.minecraft.world.level.block.OreBlock;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.FluidState;

public class OreBlocks extends OreBlock {
    private final UniformInt xpRange;

    public void DropExperience(LevelAccessor world, double x, double y, double z){
        if (world instanceof Level _level && _level.isClientSide()){
            _level.addFreshEntity(new ExperienceOrb(_level, x, y, z, this.xpRange.sample(RANDOM)));
        }
    }

    public OreBlocks(Properties properties, UniformInt experienceDrop){
        super(properties);
        this.xpRange = experienceDrop;
    }

    public OreBlocks(Properties properties){
        this(properties, UniformInt.of(0, 0));
    }

    @Override
    public int getExpDrop(BlockState state, net.minecraft.world.level.LevelReader reader, BlockPos pos, int fortune, int silktouch){
        return silktouch == 0 ? this.xpRange.sample(RANDOM) : 0;
    }

    @Override
    public void spawnAfterBreak(BlockState state, ServerLevel worldIn, BlockPos blockPos, ItemStack itemStack){
        super.spawnAfterBreak(state, worldIn, blockPos, itemStack);
    }

    @Override
    public boolean onDestroyedByPlayer(BlockState blockState, Level world, BlockPos pos, Player entity, boolean willHarvest, FluidState fluid){
        boolean retval = super.onDestroyedByPlayer(blockState, world, pos, entity, willHarvest, fluid);
        DropExperience(world, pos.getX(), pos.getY(), pos.getZ());
        return retval;
    }

    @Override
    public void wasExploded(Level world, BlockPos pos, Explosion e){
        super.wasExploded(world, pos, e);
        DropExperience(world, pos.getX(), pos.getY(), pos.getZ());
    }

 /*
    @Override
    @OnlyIn(Dist.CLIENT)
    public RenderType getRenderType(){
        return RenderType.cutout();
    }

 */
}
