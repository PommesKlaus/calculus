<template>
  <div id="app">
    <img src="../assets/logo.png">

        <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/abweichung/neu">Neue Abweichung</router-link></li>
        </ul>
        <router-view class="view"></router-view>
    <BalanceSheet></BalanceSheet>
  </div>
</template>

<script>
import BalanceSheet from './balancesheet'

export default {
  name: 'app',
  components: {
    BalanceSheet
  }
}
</script>

<style>

</style>
