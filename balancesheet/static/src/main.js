import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'

//Vue.use(Vuex)
Vue.use(VueRouter)

import router from './routes'
import store from './store'
import App from './App.vue'

new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
})
