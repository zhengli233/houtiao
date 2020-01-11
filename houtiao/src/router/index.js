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
    },
    {
      path: '/target',
      name: 'target',
      component: resolve => require(['@/pages/target'], resolve)
    },
    {
      path: '/material',
      name: 'material',
      component: resolve => require(['@/pages/material'], resolve)
    },
    {
      path: '/material2',
      name: 'material2',
      component: resolve => require(['@/pages/material2'], resolve)
    }
  ]
})
