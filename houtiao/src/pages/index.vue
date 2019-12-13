<template>
  <div>
    <el-row :gutter="0" type="flex" align="middle" class="btnGroup">
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
        <div class="btnBox">
          <el-button type="primary" icon="el-icon-menu" @click="goPage('activity')">活动</el-button>
        </div>
        <div class="btnBox">
          <el-button type="primary" icon="el-icon-s-flag" @click="goPage('target')">目标</el-button>
        </div>
        <div class="btnBox">
          <el-button type="primary" icon="el-icon-place" @click="goPage('houtiao')">猴调一下</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  methods: {
    goPage: function (name) {
      this.$router.push({name: name})
    }
  }
}
</script>

<style scoped>
  .btnGroup {
    height: 100vh;
    text-align: center;
  }
  .btnGroup .btnBox {
    margin: 10px 0;
  }
  .btnGroup .btnBox .el-button--primary {
    width: 120px;
  }
</style>
