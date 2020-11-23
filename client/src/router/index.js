import Vue from 'vue'
import Router from 'vue-router'
import Ping from '../components/Ping.vue'
import Root from '../components/Root.vue'
import Login from '../components/Login.vue'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(Router)
Vue.use(VueMaterial)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/',
      name: 'Root',
      component: Root
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
