<template>
  <div>
    <div>
      <el-button icon="el-icon-search" type="primary" @click="showAdd()" :loading="isLoading">新增</el-button>
      <el-form>
        <el-form-item label="" prop="name">
          <el-input v-model="searchForm.name" placeholder="请输入材料名称" clearable></el-input>
        </el-form-item>
        <el-form-item label="" class="lineTwoBtn lineTwoBtnBtn">
          <el-button icon="el-icon-search" type="primary" @click="search(searchForm.name)" :loading="isLoading">查询</el-button>
        </el-form-item>
      </el-form>
    </div>
    <el-table :data="tableData" height="100vh" border style="width: 100%">
      <el-table-column prop="name" label="名称">
      </el-table-column>
      <el-table-column label="">
        <template slot-scope="scope">
          <el-button round @click="showEdit(scope.row.id)" icon="el-icon-delete" :loading="isLoading">修改</el-button>
          <el-button round @click="del(scope.row.id)" icon="el-icon-delete" :loading="isLoading">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      searchForm: {},
      tableData: [
        {id: 1, name: '龙之硬币', content: [{name: '李征', target: 100, own: 65}, {name: '华晓澄', target: 80, own: 60}]}
      ]
    }
  },
  methods: {
    showAdd: function () {
    },
    showEdit: function (id) {
    },
    del: function (id) {
    }
  }
}
</script>

<style scoped>
</style>
