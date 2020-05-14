import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 要设置的全局访问的state对象
const state = {
  // token: '',
  cancelTokenArr: [],
  api: ''
}

const getters = { // 实时监听state值的变化(最新状态)
  // getToken (state) {
  //   if (state.token === '') {
  //     state.token = localStorage.getItem('token')
  //   }
  //   return state.token
  // }
}

const mutations = {
  // setToken (state, account) {
  //   state.token = account
  //   localStorage.setItem('token', account)
  // },
  pushToken (state, payload) {
    state.cancelTokenArr.push(payload.cancelToken)
  },
  clearToken (state) {
    state.cancelTokenArr.forEach(item => {
      item('路由跳转取消请求')
    })
    state.cancelTokenArr = []
  }
}

const actions = {
  // asynSetToken (context, account) {
  //   context.commit('setToken', account)
  // },
  // asynClean (context) {
  //   context.commit('setToken', '')
  //   localStorage.setItem('token', '')
  // }
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
