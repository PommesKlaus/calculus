import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import * as Cookies from 'js-cookie'

Vue.use(VueRouter)
Vue.use(VueResource)

import router from './routes'
import store from './store/index'
import App from './App.vue'

new Vue({
  router,
  store,
  el: '#app',
  render: h => h(App)
})

Vue.http.headers.common['X-CSRFToken'] = Cookies.get('csrftoken')
