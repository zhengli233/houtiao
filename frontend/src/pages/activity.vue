<template>
  <div>
    <el-table :data="tableData" class="acTable" height="100vh" border :span-method="arraySpanMethod">
      <el-table-column prop="type" label="" align="center">
      </el-table-column>
      <el-table-column v-for="item in 7" :label="'星期' + intToString(item)" :key="item" align="center">
        <template slot-scope="scope">
          <div v-if="scope.row.type !== '活动'">
            <div v-if="scope.row.weekday.indexOf(item) !== -1">{{scope.row.name}}</div>
          </div>
          <div v-else>
            <el-row>
              <el-col :span="3">{{scope.row.name}}</el-col>
              <el-col :span="4"><el-rate v-model="scope.row.level" disabled text-color="#ff9900"></el-rate></el-col>
              <el-col :span="3">{{scope.row.startDate.replace(/\//g, '-').substring(5, 10)}} - {{scope.row.endDate.replace(/\//g, '-').substring(5, 10)}}</el-col>
              <el-col :span="14" style="text-align: left; padding-left: 50px;">{{scope.row.content}}</el-col>
            </el-row>
          </div>
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
        {id: 1, name: '暗黑神殿', weekday: [1, 2, 3, 4, 5, 6, 7], type: '日常'},
        {id: 2, name: '痛苦地下室', weekday: [1, 2, 3, 4, 5, 6, 7], type: '日常'},
        {id: 3, name: '眩惑之塔', weekday: [1, 2, 3, 4, 5, 6, 7], type: '日常'},
        {id: 4, name: '第1狱', weekday: [1, 2, 3, 4, 5, 6, 7], type: '日常'},
        {id: 5, name: '第5狱', weekday: [1, 2, 3, 4, 5, 6, 7], type: '日常'},
        {id: 6, name: '中央竞技场', weekday: [1], type: '日常'},
        {id: 7, name: '扭曲世界的次元', weekday: [4], type: '日常'},
        {id: 8, name: '红玉的诅咒', weekday: [4], type: '日常'},
        {id: 9, name: '超时空漩涡', weekday: [2, 3], type: '副本'},
        {id: 10, name: '普雷·伊希斯', weekday: [6, 7], type: '副本'},
        {id: 11, name: '魔界大战', weekday: [4, 5], type: '副本'},
        {id: 12, name: '洞察之眼', weekday: [4, 5], type: '副本'},
        {id: 13, name: '公会庆典', weekday: [4, 5], type: '公会'},
        {id: 14, name: '攻坚商店', weekday: [4, 5], type: '商店'},
        {id: 15, name: '公会商店', weekday: [4, 5], type: '商店'},
        {id: 16, name: '探秘瓦尔哈拉', weekday: [], type: '活动', level: 3, startDate: '2020/05/07', endDate: '2020/06/04', content: 'buff宝珠，附魔等'},
        {id: 17, name: '积分商城', weekday: [], type: '活动', level: 2.5, startDate: '2020/04/23', endDate: '2020/06/04', content: 'buff光环、通行证、赛丽亚的灿烂幸运等'},
        {id: 18, name: '再战安徒恩', weekday: [], type: '活动', level: 4, startDate: '2020/05/21', endDate: '2020/07/16', content: '引导石，85ss套，100ss武器，灼炎荒古装扮'},
        {id: 19, name: '冒险家回归', weekday: [], type: '活动', level: 3, startDate: '2020/05/21', endDate: '2020/07/16', content: '12期天空，+10增幅券等'},
        {id: 20, name: '强者之路：抉择', weekday: [], type: '活动', level: 3, startDate: '2020/05/21', endDate: '2020/07/16', content: '新增匹配模式，武器装扮，光环，护石符文，袖珍罐等'},
        {id: 21, name: '逆转的次元', weekday: [], type: '活动', level: 2, startDate: '2020/05/21', endDate: '2020/06/18', content: '动漫联动远古&异界地下城，附魔，灵魂武器，称号，边框等'},
        {id: 22, name: '幸运卡券', weekday: [], type: '活动', level: 5, startDate: '2020/05/21', endDate: '2020/06/04', content: '引导石，强化券'},
        {id: 23, name: '智慧之光', weekday: [], type: '活动', level: 5, startDate: '2020/05/21', endDate: '2020/06/18', content: '引导石'},
        {id: 24, name: '公会你我他', weekday: [], type: '活动', level: 1, startDate: '2020/05/21', endDate: '2020/06/04', content: '公会硬币'},
        {id: 25, name: '寻宝乐翻天', weekday: [], type: '活动', level: 2, startDate: '2020/05/21', endDate: '2020/06/18', content: '刮刮乐附魔'}
      ]
    }
  },
  methods: {
    intToString: function (int) {
      switch (int) {
        case 1:
          return '一'
        case 2:
          return '二'
        case 3:
          return '三'
        case 4:
          return '四'
        case 5:
          return '五'
        case 6:
          return '六'
        case 7:
          return '日'
      }
    },
    arraySpanMethod ({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        if (rowIndex === 0) {
          return [8, 1]
        } else if ([1, 2, 3, 4, 5, 6, 7].indexOf(rowIndex) !== -1) {
          return [0, 0]
        } else if (rowIndex === 8) {
          return [4, 1]
        } else if ([9, 10, 11].indexOf(rowIndex) !== -1) {
          return [0, 0]
        } else if (rowIndex === 13) {
          return [2, 1]
        } else if ([14].indexOf(rowIndex) !== -1) {
          return [0, 0]
        } else if (rowIndex === 15) {
          return [10, 1]
        } else if ([16, 17, 18, 19, 20, 21, 22, 23, 24].indexOf(rowIndex) !== -1) {
          return [0, 0]
        }
      } else if (columnIndex === 1) {
        if ([15, 16, 17, 18, 19, 20, 21, 22, 23, 24].indexOf(rowIndex) !== -1) {
          return [1, 7]
        }
      } else {
        if ([15, 16, 17, 18, 19, 20, 21, 22, 23, 24].indexOf(rowIndex) !== -1) {
          return [0, 0]
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
