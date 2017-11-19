import Vue from 'vue'
import Router from 'vue-router'
import layout from '@/components/layout'
import login from '@/components/login'
import bookUpload from '@/components/bookUpload'
import bookList from '@/components/bookList'
import userNormal from '@/components/userNormal'
import userManage from '@/components/userManage'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'layout',
      component: layout,
      children: [
        {
          path: '/bookUpload',
          name: 'bookUpload',
          component: bookUpload
        },
        {
          path: '/bookList',
          name: 'bookList',
          component: bookList
        },
        {
          path: '/userNormal',
          name: 'userNormal',
          component: userNormal
        },
        {
          path: '/userManage',
          name: 'userManage',
          component: userManage
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
