<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
    <FindHoutiao></FindHoutiao>
  </div>
</template>

<script>
import FindHoutiao from './components/FindHoutiao'
export default {
  name: 'App',
  components: {
    FindHoutiao
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
