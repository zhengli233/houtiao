<template>
  <div>
    <el-button v-on:click='toActivityPage'>活动</el-button>
    <el-button v-on:click='toHoutiaoPage'>猴调一下</el-button>
  </div>
</template>>

<script>
export default {
  methods: {
    toActivityPage: function () {
      this.$router.push({name: 'activity'})
    },
    toHoutiaoPage: function () {
      this.$router.push({name: 'houtiao'})
    }
  }
}
</script>
