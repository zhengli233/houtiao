// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI, {Message} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.prototype.axios = axios
Vue.use(VueAxios, axios)
Vue.use(ElementUI)

Vue.config.productionTip = false

// 路由拦截
router.beforeEach((to, from, next) => {
  store.commit('clearToken') // 取消请求
  next()
})

// 请求拦截
axios.interceptors.request.use(config => {
  // if (store.getters.getToken !== '' && store.getters.getToken !== null) { // 如果token非空，请求时带上token
  //   config.headers.Authorization = store.getters.getToken
  // }
  config.cancelToken = new axios.CancelToken(function (cancel) {
    store.commit('pushToken', {cancelToken: cancel})
  })
  return config
})

// 响应拦截
axios.interceptors.response.use((response) => {
  if (response.data.success === false) {
    Message({
      type: 'error',
      message: response.data.errorMessage
    })
  } else {
    return response
  }
}, function (error) {
  if (axios.isCancel(error)) { // 为了终结promise链 就是实际请求不会走到.catch(rej=>{});这样就不会触发错误提示之类了
    return new Promise(() => {})
  } else {
    Message({
      message: '服务器内部错误！',
      type: 'error'
    })
  }
  return Promise.reject(error)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
