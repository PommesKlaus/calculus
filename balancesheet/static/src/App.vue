<template>
  <div id="app" class="container-fluid">
    <h1>Übersicht steuerbilanzielle Abweichungen <span v-if="Status > 0"><img src="./assets/ajax-loader.gif"></span></h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {}
  },
  computed: {
    Status () {
      return this.$store.state.Status
    }
  }
}
</script>

<style>
.form-control:invalid {
  border: 3px solid #f44336;
}
</style>
