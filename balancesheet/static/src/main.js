import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import TestComponent from './components/test1.vue'
import BalanceSheet from './components/balancesheet.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/foo', component: TestComponent },
  { path: '/', component: BalanceSheet }
]

const router = new VueRouter({
  routes
})

new Vue({
  router,
  el: '#app',
  render: h => h(App)
})
