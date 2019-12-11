<template>
  <div>
    <el-button type='primary' icon='el-icon-search' :loading='isLoading' @click='getMonkeyTwig()'>找到猴调的人</el-button>
    <input v-model='monkeyTwigName'><br>
    <el-table
      :data='table'
      stripe
      fit
      ref='singleTable'
      tooltip-effect='dark'
      style='width: 100%'>
      <template v-for='(col) in tableTitle'>
        <el-table-column
          :show-overflow-tooltip='true'
          :prop='col.col'
          :label='col.title'
          :key='col.col'
        >
        </el-table-column>
      </template>
      <el-table-column
        label='action'
      >
        <template slot-scope='scope'>
          <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">delete</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-button v-on:click='addHoutiaoPerson'>添加一个猴调的人</el-button>
    <el-button v-on:click='setMonkeyTwig'>记录猴调的人</el-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isLoading: false,
      monkeyTwigName: 'Hua Xiaocheng',
      table: [],
      tableTitle: [{
        col: 'name',
        title: '猴调的人名'
      }, {
        col: 'level',
        title: '猴调的程度'
      }, {
        col: 'time',
        title: '猴调的时间'
      }]
    }
  },
  mounted: function () {
    this.getMonkeyTwig()
  },
  methods: {
    getMonkeyTwig: function () {
      this.isLoading = true
      this.axios.get('/api/houtiao_person').then(res => {
        console.log('猴调成功', res)
        this.table = res.data
        this.isLoading = false
      }).catch(err => {
        console.log('猴调出错', err)
        this.isLoading = false
      })
    },
    setMonkeyTwig: function () {
      this.axios.post('/api/set_houtiao_people', {
        name: this.monkeyTwigName,
        level: 'normal'
      }).then(res => {
        console.log('记录一个猴调的人成功')
      }).catch(err => {
        console.log('猴调出错', err)
      })
    },
    cellEditDone: function (newValue, oldValue, rowIndex, rowData, field) {
      this.tableData[rowIndex][field] = newValue
    },
    handleDelete: function (index, row) {
      this.axios.post('/api/delete_houtiao', {
        name: row.name
      }).then(res => {
        console.log('删除一个猴调的人成功')
      }).catch(err => {
        console.log('猴调出错', err)
      })
      this.getMonkeyTwig()
    },
    addHoutiaoPerson: function () {
    }
  }
}
</script>
