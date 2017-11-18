import Vue from 'vue'
import Router from 'vue-router'
import read from '@/components/read'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'read',
      component: read 
    }
  ]
})
