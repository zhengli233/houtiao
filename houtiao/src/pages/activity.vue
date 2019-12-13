<template>
  <div>
    <el-table :data="tableData" height="100vh" border style="width: 100%">
      <el-table-column prop="name" label="活动名称">
      </el-table-column>
      <el-table-column prop="date" label="活动日期">
      </el-table-column>
      <el-table-column prop="content" label="简述">
      </el-table-column>
      <el-table-column label="完成" width="100">
        <template slot-scope="props">
          <el-button type="primary" icon="el-icon-check" size="mini" @click="finishTask(props.row.id)">完成</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      tableData: [
        {id: 1, name: '眩惑之塔', date: '常驻', content: '每周四刷新，一周7次，一天1次'},
        {id: 2, name: '泰波尔斯引导', date: '常驻', content: '每周四刷新，一周6次，一天3次'},
        {id: 3, name: '超时空漩涡单人本', date: '常驻', content: '每周二刷新，一周2次，一天1次'},
        {id: 4, name: '代号·希望', date: '常驻', content: '每周一刷新，一周3次，一天3次'},
        {id: 5, name: '中央竞技场', date: '常驻', content: '每周一刷新，一周3次，一天1次'},
        {id: 6, name: '周常地下城', date: '常驻', content: '每周四刷新，一周3次，一天3次'},
        {id: 7, name: '灾难领域', date: '常驻', content: '每周二刷新，一周10次，一天10次'},
        {id: 8, name: '周末签到享惊喜', date: '2019.11.28~2020.1.14（还剩两周）', content: '每周末签到'},
        {id: 9, name: '阳光少女成长记', date: '2019.11.28~2019.12.24（还剩两周）', content: '兑换强打书'},
        {id: 10, name: '史诗之路', date: '2019.12.10~2020.1.14（五周）', content: '每天3+4次，每周四刷新商店，兑换强打书、黑瞳石'},
        {id: 11, name: '南瓜球的新商机', date: '2019.12.10~2020.1.14（五周）', content: '史诗之路材料兑换强打书'},
        {id: 12, name: '冒险者的游戏', date: '2019.12.10~2020.1.14（五周）', content: '每天2次，不能2次都最后一名'},
        {id: 13, name: '休息，休息一会', date: '2019.12.10~2020.1.14（五周）', content: '每周四刷新商店'},
        {id: 14, name: '雪球奇缘', date: '2019.12.10~2020.1.14（五周）', content: '每天3次，每周四刷新商店'},
        {id: 15, name: '阿拉德探险记', date: '2019.12.10~2020.3.19（100天）', content: '每周四刷新每周任务'}
      ]
    }
  },
  methods: {
    finishTask: function (id) {
      console.log(id)
      this.tableData = this.tableData.filter(item => item.id !== id)
    }
  }
}
</script>

<style scoped>

</style>
