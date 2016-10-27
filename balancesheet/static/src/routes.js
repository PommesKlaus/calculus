import VueRouter from 'vue-router'
import TestComponent from './components/test1.vue'
import BalanceSheet from './components/balancesheet.vue'

const routes = [
  { path: '/foo', component: TestComponent },
  { path: '/', component: BalanceSheet }
]

const router = new VueRouter({
  routes
})

export default router