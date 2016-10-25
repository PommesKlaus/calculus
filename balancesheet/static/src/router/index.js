import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

import BalanceSheet from '../components/balancesheet.vue';
import DifferenceDetail from '../components/differencedetail.vue';

export const routes = [
    {path: '/', component: BalanceSheet},
    {path: '/abweichung/neu', component: DifferenceDetail},
    {path: '/abweichung/:differenceId(\\d+)', component: DifferenceDetail}
];

export const router = new Router({
    mode: 'history',
    routes
});
