<template>
    <div id="FindHoutiao">
    <h1>{{ houtiao_name }}</h1>
    <input v-model="houtiao_name"><br>
    <button v-on:click="getHoutiao">找到猴调的人</button>
    </div>
</template>

<script>
import Vue from 'vue'
export default {
  name: 'FindHoutiao',
  data () {
    return {
      houtiao_name: 'Hua Xiaocheng'
    }
  },
  methods: {
    getHoutiao: function () {
      Vue.http.get('/houtiao_person').then((response) => {
        this.houtiao_name = response.json()
      }, (response) => {}
      )
    }
  }
}
</script>
