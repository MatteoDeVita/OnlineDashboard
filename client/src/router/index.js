import Vue from 'vue'
import Router from 'vue-router'
import Ping from '../components/Ping.vue'
import Root from '../components/Root.vue'
import Login from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'
import About from '../components/About'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import VueFab from 'vue-float-action-button'
import VueYoutube from 'vue-youtube'

import JsonViewer from 'vue-json-viewer'

Vue.use(Router)
Vue.use(VueMaterial)
Vue.use(VueFab)
Vue.use(VueYoutube)
Vue.use(JsonViewer)

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
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/about.json',
      name: 'About',
      component: About
    }
  ]
})
