import Vue from 'vue'
import App from './components/App.vue'
import router from './router';

new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: { App }
})
