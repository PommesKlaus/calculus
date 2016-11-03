import VueRouter from 'vue-router'
import BalanceSheet from './components/balancesheet.vue'
import Details from './components/details.vue'
// import NewDiff from './components/new.vue'

const routes = [
  { 
    path: '/', 
    name: 'balancesheet',
    component: BalanceSheet 
  },
  { 
    path: '/neu', 
    name: 'differenceNew',
    component: Details
  },
  { 
    path: '/details/:differenceId', 
    name: 'differenceDetails',
    component: Details 
  }  
]

const router = new VueRouter({
  routes
})

export default router