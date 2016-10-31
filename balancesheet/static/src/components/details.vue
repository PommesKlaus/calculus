<template>
  <div class="container">
    <form v-on:submit.prevent="onSubmit">
  
      <div class="col-md-2">Bilanzlinie:</div>
      <div class="col-md-10">Bla Bla</div>
  
      <div class="col-md-2">Sachverhalt:</div>
      <div class="col-md-10">{{ formData.name }}</div>
  
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
            <td>{{ formData.py_local_gaap }}</td>
            <td></td>
            <td>{{ formData.tu_local_gaap }}</td>
            <td></td>
            <td><input v-model="formData.local_gaap" class="form-control"></td>
          </tr>
          <tr>
            <td>Tax GAAP</td>
            <td>{{ formData.py_tax_gaap }}</td>
            <td></td>
            <td>{{ formData.tu_tax_gaap }}</td>
            <td></td>
            <td><input v-model="formData.tax_gaap" class="form-control"></td>
          </tr>
          <tr>
            <td>Differenz</td>
            <td>{{ formData.py_difference }}</td>
            <td></td>
            <td>{{ formData.tu_difference }}</td>
            <td></td>
            <td>{{ formData.difference }}</td>
          </tr>
        </tbody>
      </table>
      
      <h2>Erfolgswirksame Veränderungen</h2>
      <table class="table table-hover">
        <thead>
          <tr>
            <th class="col-md-2"></th>
            <th class="col-md-2"></th>
            <th class="col-md-2">Matching</th>
            <th class="col-md-2"></th>
            <th class="col-md-2">Gewinnauswirkung</th>
            <th class="col-md-2"></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>StB-Gewinnauswirkung</td>
            <td></td>
            <td>{{ formData.pl_true_up }}</td>
            <td></td>
            <td>{{ formData.pl_movement }}</td>
            <td></td>
          </tr>
        </tbody>
      </table>
      
      <button type="submit">Speichern</button>
    </form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import * as types from '../store/mutation-types'

module.exports = {
  data: function() {
    return {
      formData: {}
    }
  },
  methods: {
    onSubmit (e) {
      return this.$store.dispatch('updateDifference', {difference: this.difference, formData: this.formData})
    }
  },
  computed: {
    difference () {
        let r = this.$route.params.differenceId
        return this.$store.state.Differences.find(function(x) { return x.id == r })
    },
    lineItems() { return this.$store.state.LineItems }
  },
  created() {
    // Copy difference-data from state to be used as form model.
    // Changes are only merged to state/store if form is submitted.
    this.formData = Object.assign({}, this.difference)
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