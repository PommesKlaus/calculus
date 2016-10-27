<template>
  <div class="container">
    <div class="col-md-2">Bilanzlinie:</div>
    <div class="col-md-10">Bla Bla</div>

    <div class="col-md-2">Sachverhalt:</div>
    <div class="col-md-10">{{ difference.name }}</div>

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
          <td>{{ difference.py_local_gaap }}</td>
          <td></td>
          <td>{{ difference.tu_local_gaap }}</td>
          <td></td>
          <td>{{ difference.local_gaap }}</td>
        </tr>
        <tr>
          <td>Tax GAAP</td>
          <td>{{ difference.py_tax_gaap }}</td>
          <td></td>
          <td>{{ difference.tu_tax_gaap }}</td>
          <td></td>
          <td>{{ difference.tax_gaap }}</td>
        </tr>
        <tr>
          <td>Differenz</td>
          <td>{{ difference.py_difference }}</td>
          <td></td>
          <td>{{ difference.tu_difference }}</td>
          <td></td>
          <td>{{ difference.difference }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState } from 'vuex'
module.exports = {  
  data: function() {
    return {
      }
  },
  computed: mapState({
    Differences: 'Differences',
    difference (state) {
      let r = this.$route.params.differenceId
      return state.Differences.find(function(x) { return x.id == r })
    },
    LineItems: 'LineItems'
  })
}
</script>

<style scoped>
th {
  text-align: center;
}
td:nth-child(n+2) {
  text-align: right;
}
</style>