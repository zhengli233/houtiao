import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: resolve => require(['@/pages/index'], resolve)
    },
    {
      path: '/houtiao',
      name: 'houtiao',
      component: resolve => require(['@/pages/houtiao'], resolve)
    },
    {
      path: '/activity',
      name: 'activity',
      component: resolve => require(['@/pages/activity'], resolve)
    }
  ]
})
