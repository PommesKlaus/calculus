<template>
  <div class="container">
    <form v-on:submit.prevent="onSubmit">
  
      <div class="col-md-2">Bilanzlinie:</div>
      <div class="col-md-10">Bla Bla</div>
  
      <div class="col-md-2">Sachverhalt:</div>
      <div class="col-md-10"></div>
  
      <table class="table table-hover">
        <thead>
          <tr>
            <th class="col-md-2"></th>
            <th class="col-md-2">Vorperiode</th>
            <th class="col-md-2"></th>
            <th class="col-md-2">Matching Vorperiode</th>
            <th class="col-md-2"></th>
            <th class="col-md-2">lfd. Periode</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Local GAAP</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td><input v-model.lazy="formData.local_gaap" class="form-control input-sm"></td>
          </tr>
          <tr>
            <td>Tax GAAP</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td><input v-model="formData.tax_gaap" class="form-control input-sm"></td>
          </tr>
          <tr>
            <td>Differenz</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </table>
    </form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
module.exports = {
  data: function() {
    return {
      formData: {}
    }
  },
  methods: {
    onSubmit () {
      return
    }
  },
  computed: {
    Difference () {
        let r = this.$route.params.differenceId
        return this.$store.state.Differences.find(function(x) { return x.id == r })
    },
    LineItems() { return this.$store.state.LineItems }
  },
  created() {
    // Copy difference-data from state to be used as form model.
    // Changes are only merged to state/store if form is submitted.
    this.formData = Object.assign({}, this.Difference)
  }
}
</script>

<style scoped>
th {
  text-align: center;
}

td:nth-child(n+2) {
  text-align: right;
}

td:nth-child(n+2) input {
  text-align: right;
}
</style>