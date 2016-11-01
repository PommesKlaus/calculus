<template>
  <div class="container">
    <form v-on:submit.prevent="onSubmit">
  
      <div class="col-md-2">Bilanzlinie:</div>
      <div class="col-md-10">Bla Bla</div>
  
      <div class="col-md-2">Sachverhalt:</div>
      <div class="col-md-10">{{ formData.name }}</div>
      
      <h2>Gesamtdifferenz Local GAAP/Tax GAAP</h2>
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
      
      <h2>davon <strong>erfolgswirksam</strong></h2>
      <table class="table table-hover">
        <thead>
          <tr>
            <th class="col-md-2"></th>
            <th class="col-md-2">Vorperiode</th>
            <th class="col-md-2">Matching</th>
            <th class="col-md-2">Matching Vorperiode</th>
            <th class="col-md-2">Gewinnauswirkung</th>
            <th class="col-md-2">lfd. Periode</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>temporär</td>
            <td>{{ formData.py_pl_temporary }}</td>
            <td></td>
            <td>{{ formData.tu_pl_temporary }}</td>
            <td></td>
            <td>{{ formData.pl_temporary }}</td>
          </tr>
          <tr>
            <td>permanent</td>
            <td>{{ formData.py_pl_permanent }}</td>
            <td></td>
            <td>{{ formData.tu_pl_permanent }}</td>
            <td></td>
            <td><input v-model="formData.pl_permanent" class="form-control"></td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td>erfolgswirksam</td>
            <td>{{ formData.py_pl }}</td>
            <td><strong>{{ formData.pl_true_up }}</strong></td>
            <td>{{ formData.tu_pl }}</td>
            <td><strong>{{ formData.pl_movement }}</strong></td>
            <td>{{ formData.pl }}</td>
          </tr>
        </tfoot>
      </table>

      <h2>davon <strong>erfolgsneutral</strong></h2>
      <table class="table table-hover">
        <thead>
          <tr>
            <th class="col-md-2"></th>
            <th class="col-md-2">Vorperiode</th>
            <th class="col-md-2">Matching</th>
            <th class="col-md-2">Matching Vorperiode</th>
            <th class="col-md-2">Gewinnauswirkung</th>
            <th class="col-md-2">lfd. Periode</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>temporär</td>
            <td>{{ formData.py_oci_temporary }}</td>
            <td></td>
            <td>{{ formData.tu_oci_temporary }}</td>
            <td></td>
            <td><input v-model="formData.oci_temporary" class="form-control"></td>
          </tr>
          <tr>
            <td>permanent</td>
            <td>{{ formData.py_oci_permanent }}</td>
            <td></td>
            <td>{{ formData.tu_oci_permanent }}</td>
            <td></td>
            <td><input v-model="formData.oci_permanent" class="form-control"></td>
          </tr>
        </tbody>
        <tfoot>
          <tr>
            <td>erfolgsneutral</td>
            <td>{{ formData.py_oci }}</td>
            <td><strong>{{ formData.oci_true_up }}</strong></td>
            <td>{{ formData.tu_oci }}</td>
            <td><strong>{{ formData.oci_movement }}</strong></td>
            <td>{{ formData.oci }}</td>
          </tr>
        </tfoot>
      </table>

      <div class="col-md-12">
        <textarea v-model="formData.comment" placeholder="Kurze Beschreibung des Sachverhalts" class="form-control" rows="5"></textarea>
      </div>
      
      <button type="submit" class="btn btn-success center">Speichern</button>
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