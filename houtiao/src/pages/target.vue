<template>
  <div>
    <el-table :data="tableData" height="625px" border style="width: 100%">
      <el-table-column prop="name" label="部位">
      </el-table-column>
      <el-table-column prop="target" label="目标">
      </el-table-column>
      <el-table-column prop="strengthen" label="强化/增幅">
      </el-table-column>
      <el-table-column prop="enchanting" label="附魔">
      </el-table-column>
      <el-table-column prop="badge" label="徽章">
      </el-table-column>
    </el-table>
    <p class="title">除武器外，各部位泰波尔斯升级到普雷后提升对比</p>
    <el-row :gutter="0" class="picGroup">
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <el-image class="pic" src="../../static/images/order_leather.png"></el-image>
      </el-col>
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <el-image class="pic" src="../../static/images/order_light.png"></el-image>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      tableData: [
        {id: 1, name: '护肩', target: '超界', strengthen: '增幅7（力28）', enchanting: '力50（反物质粒子）', badge: '黄：释放（0.9/1.6/2.2）/攻速（0.6/1.1/1.5）'},
        {id: 2, name: '上衣', target: '超界', strengthen: '增幅7（力28）', enchanting: '攻45力15（中央竞技场）', badge: '绿：暴（1.1/2.2/3.0）/避（0.8/1.1/1.5）'},
        {id: 3, name: '下装', target: '超界', strengthen: '增幅7（力28）', enchanting: '攻45力15（中央竞技场）', badge: '绿：暴（1.1/2.2/3.0）/避（0.8/1.1/1.5）'},
        {id: 4, name: '腰带', target: '超界', strengthen: '增幅7（力28）', enchanting: '力50（反物质粒子）', badge: '红：力（10/17/25）'},
        {id: 5, name: '鞋', target: '超界', strengthen: '增幅7（力28）', enchanting: '力50（反物质粒子）', badge: '蓝：命（0.6/1.1/1.5）/移速（0.6/1.1/1.5）'},
        {id: 6, name: '武器', target: '夜语黑瞳（228黑瞳石）', strengthen: '强化12（攻697）', enchanting: '攻45力15（中央竞技场）', badge: '/'},
        {id: 7, name: '手镯', target: '江山如画', strengthen: '增幅7（力28）', enchanting: '单属强25（大富翁）', badge: '蓝：命（0.6/1.1/1.5）/移速（0.6/1.1/1.5）'},
        {id: 8, name: '戒指', target: '江山如画', strengthen: '增幅7（力28）', enchanting: '单属强20（大富翁）', badge: '红：力（10/17/25）'},
        {id: 9, name: '项链', target: '江山如画', strengthen: '增幅7（力28）', enchanting: '单属强20（大富翁）', badge: '黄：释放（0.9/1.6/2.2）/攻速（0.6/1.1/1.5）'},
        {id: 10, name: '辅助装备', target: '万物的生灭', strengthen: '增幅7（力28+17）', enchanting: '三攻50（大富翁）', badge: '白：技能lv'},
        {id: 11, name: '魔法石', target: '万物的生灭', strengthen: '增幅7（力28+17）', enchanting: '全属强20（大富翁）', badge: '白：技能lv'},
        {id: 12, name: '耳环', target: '万物的生灭', strengthen: '强化10（三攻45）', enchanting: '四维80（大富翁）', badge: '/'}
      ]
    }
  },
  methods: {
  }
}
</script>

<style scoped>
  .title {
    text-align: center;
    margin: 20px 100px;
    font-size: 16px;
    font-weight: bold;
    line-height: 32px;
    border-bottom: 1px solid #ccc;
  }
  .picGroup {
    text-align: center;
  }
  .picGroup .pic {
    width: 358px;
    height: 158px;
  }
</style>
