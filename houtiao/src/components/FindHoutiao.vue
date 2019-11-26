<template>
    <div>
    <h1>{{ monkeyTwigName }}</h1>
    <button v-on:click="getMonkeyTwig()">找到猴调的人</button>
    </div>
</template>

<script>
export default {
  data () {
    return {
      monkeyTwigName: 'Hua Xiaocheng'
    }
  },
  methods: {
    getMonkeyTwig: function () {
      this.axios.get('/houtiao_person').then(res => {
        console.log('猴调，对的', res)
        this.monkeyTwigName = res.data.data.name
      }).catch(err => {
        console.log('猴调，出错了', err)
      })
    }
  }
}
</script>
