<template>
  <div id="app">
    <h1>Übersicht steuerbilanzielle Abweichungen</h1>
    <balance-sheet></balance-sheet>
  </div>
</template>

<script>
import BalanceSheet from './components/balancesheet.vue';

export default {
  name: 'app',
  data () {
    return {
      
    }
  },
  components: {
    BalanceSheet
  }
}
</script>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
