<template>
    <div>
        <h1>BILANZ</h1>
        <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/abweichung/neu">Neue Abweichung</router-link></li>
        </ul>
        <router-view class="view"></router-view>
    </div>
</template>

<script>
export default {
  name: 'BalanceSheet'  
}
</script>

<style scoped>

</style>
