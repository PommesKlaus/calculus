<template>
  <div class="container">
    <form v-on:submit.prevent="onSubmit">
  
      <div class="col-md-2">Bilanzlinie:</div>
      <div class="col-md-10">{{ lineItem.name }}</div>
  
      <div class="col-md-2">Sachverhalt:</div>
      <div class="col-md-10">{{ formData.name }}</div>
      
      <h2>Gesamtdifferenz Local GAAP/Tax GAAP</h2>
      <table class="table table-hover">
        <thead>
          <tr>
            <th class="col-md-2"></th>
            <th class="col-md-2">{{ version.py_year }}<br />{{ version.py_shortname }}</th>
            <th class="col-md-2"></th>
            <th class="col-md-2">{{ version.tu_year }}<br />{{ version.tu_shortname }}</th>
            <th class="col-md-2"></th>
            <th class="col-md-2">{{ version.year }}<br />{{ version.shortname }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Local GAAP</td>
            <td>{{ formData.py_local_gaap }}</td>
            <td></td>
            <td>{{ formData.tu_local_gaap }}</td>
            <td></td>
            <td><input v-model="formData.local_gaap" class="form-control" pattern="^[-]?[0-9]((\d+([,]\d{0,2})?$)|(\d{0,2}(?:\.\d{3})*([,]\d{0,2})?))$"></td>
          </tr>
          <tr>
            <td>Tax GAAP</td>
            <td>{{ formData.py_tax_gaap }}</td>
            <td></td>
            <td>{{ formData.tu_tax_gaap }}</td>
            <td></td>
            <td><input v-model="formData.tax_gaap" class="form-control" pattern="^[-]?[0-9]((\d+([,]\d{0,2})?$)|(\d{0,2}(?:\.\d{3})*([,]\d{0,2})?))$"></td>
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
            <th class="col-md-2">{{ version.py_year }}<br />{{ version.py_shortname }}</th>
            <th class="col-md-2">Matching</th>
            <th class="col-md-2">{{ version.tu_year }}<br />{{ version.tu_shortname }}</th>
            <th class="col-md-2">Gewinnauswirkung</th>
            <th class="col-md-2">{{ version.year }}<br />{{ version.shortname }}</th>
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
            <td><input v-model="formData.pl_permanent" class="form-control" pattern="^[-]?[0-9]((\d+([,]\d{0,2})?$)|(\d{0,2}(?:\.\d{3})*([,]\d{0,2})?))$"></td>
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
            <th class="col-md-2">{{ version.py_year }}<br />{{ version.py_shortname }}</th>
            <th class="col-md-2">Matching</th>
            <th class="col-md-2">{{ version.tu_year }}<br />{{ version.tu_shortname }}</th>
            <th class="col-md-2">Gewinnauswirkung</th>
            <th class="col-md-2">{{ version.year }}<br />{{ version.shortname }}</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>temporär</td>
            <td>{{ formData.py_oci_temporary }}</td>
            <td></td>
            <td>{{ formData.tu_oci_temporary }}</td>
            <td></td>
            <td><input v-model="formData.oci_temporary" class="form-control" pattern="^[-]?[0-9]((\d+([,]\d{0,2})?$)|(\d{0,2}(?:\.\d{3})*([,]\d{0,2})?))$"></td>
          </tr>
          <tr>
            <td>permanent</td>
            <td>{{ formData.py_oci_permanent }}</td>
            <td></td>
            <td>{{ formData.tu_oci_permanent }}</td>
            <td></td>
            <td><input v-model="formData.oci_permanent" class="form-control" pattern="^[-]?[0-9]((\d+([,]\d{0,2})?$)|(\d{0,2}(?:\.\d{3})*([,]\d{0,2})?))$"></td>
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
        let r = this.$route.params.differenceId || null
        if (r === null) {
          return {
            name: "",
            comment: "",
            bs_line_item_id: null,
            version_id: this.$store.state.Version.id,

            local_gaap: "0,00",
            tax_gaap: "0,00",
            difference: "0,00",
            pl_permanent: "0,00",
            oci_permanent: "0,00",
            permanent: "0,00",
            pl_temporary: "0,00",
            oci_temporary: "0,00",
            temporary: "0,00",
            pl: "0,00",
            oci: "0,00",

            py_local_gaap: "0,00",
            py_tax_gaap: "0,00",
            py_difference: "0,00",
            py_pl_permanent: "0,00",
            py_oci_permanent: "0,00",
            py_permanent: "0,00",
            py_pl_temporary: "0,00",
            py_oci_temporary: "0,00",
            py_temporary: "0,00",
            py_pl: "0,00",
            py_oci: "0,00",

            tu_local_gaap: "0,00",
            tu_tax_gaap: "0,00",
            tu_difference: "0,00",
            tu_pl_permanent: "0,00",
            tu_oci_permanent: "0,00",
            tu_permanent: "0,00",
            tu_pl_temporary: "0,00",
            tu_oci_temporary: "0,00",
            tu_temporary: "0,00",
            tu_pl: "0,00",
            tu_oci: "0,00",

            pl_true_up: "0,00",
            oci_true_up: "0,00",
            pl_movement: "0,00",
            oci_movement: "0,00",
          }
        } else {
          return this.$store.state.Differences.find(function(x) { return x.id == r })
        }
    },
    lineItems() { return this.$store.state.LineItems },
    lineItem() {
      const d = this.difference
      if (d.bs_line_item_id !== null) {
        return this.$store.state.LineItems.find(function(x) { return x.id == d.bs_line_item_id })
      } else {
        return {}
      }
    },
    version() { return this.$store.state.Version }
  },
  mounted() {
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