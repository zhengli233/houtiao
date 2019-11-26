<template>
  <div>
    <el-button type="primary" icon="el-icon-search" :loading="isLoading" @click="getMonkeyTwig()">找到猴调的人</el-button>
    <h1>{{ monkeyTwigName }}</h1>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isLoading: false,
      monkeyTwigName: 'Hua Xiaocheng'
    }
  },
  methods: {
    getMonkeyTwig: function () {
      this.isLoading = true
      this.axios.get('/api/houtiao_person').then(res => {
        console.log('猴调成功', res)
        this.monkeyTwigName = res.data.name
        this.isLoading = false
      }).catch(err => {
        console.log('猴调出错', err)
        this.isLoading = false
      })
    }
  }
}
</script>
