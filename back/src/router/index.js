import Vue from 'vue'
import Router from 'vue-router'
import layout from '@/components/layout'
import login from '@/components/login'
import bread from '@/components/breadCrumb'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'layout',
      component: layout
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
