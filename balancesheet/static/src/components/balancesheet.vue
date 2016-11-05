<template>
  <div>
    <p>
      Vorjahr: {{ Version.py_year }}, {{ Version.py_name }} ({{ Version.py_shortname }})<br />
      Matching: {{ Version.tu_year }}, {{ Version.tu_name }} ({{ Version.tu_shortname }})<br />
      lfd. jahr: {{ Version.year }}, {{ Version.name }} ({{ Version.shortname }})
    </p>
    <table class="table table-hover table-condensed table-bordered balancesheet">
      <thead>
        <tr>
          <th class="balance-sheet-icon-col"></th>
          <th></th>
          <th>Local</th>
          <th>Tax</th>
          <th>Differenz</th>
          <th>Matching</th>
          <th>Gewinn</th>
        </tr>
      </thead>
      <tbody v-for="item in LineItems">
        <tr>
          <td class="balance-sheet-icon-col subtotal"></td>
          <td class="line-label subtotal">{{ item.name }}</td>
          <td class="subtotal"></td>
          <td class="subtotal"></td>
          <td class="subtotal">{{ item.subtotal_difference }}</td>
          <td class="subtotal">{{ item.subtotal_pl_true_up }}</td>
          <td class="subtotal">{{ item.subtotal_pl_movement }}</td>
        </tr>
       
        <tr v-for="dif in filteredDifferences(item.id, Differences)">
          <td class="balance-sheet-icon-col"></td>
          <td class="line-label"><div class="bs_dif">
            <router-link :to="{ name: 'differenceDetails', params: {differenceId: dif.id}}" >{{ dif.name }}</router-link>
            </div></td>
          <td>{{ dif.local_gaap }}</td>
          <td>{{ dif.tax_gaap }}</td>
          <td>{{ dif.difference }}</td>
          <td>{{ dif.pl_true_up }}</td>
          <td>{{ dif.pl_movement }}</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <th class="balance-sheet-icon-col">SUMME</th>
          <th></th>
          <th></th>
          <th></th>
          <th class="">{{ Totals.difference__sum }}</th>
          <th class="">{{ Totals.pl_true_up__sum }}</th>
          <th class="">{{ Totals.pl_movement__sum }}</th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>
import { mapState } from 'vuex'
module.exports = {
  data: function() {
    return {}
  },
  methods:  {
    filteredDifferences: function(lineItemId, differences) {
      return differences.filter(function (x) {
        return x.bs_line_item_id === lineItemId;
      });
    }
  },
  computed: mapState([
    'Differences',
    'LineItems',
    'Totals',
    'Version'
  ])
}
</script>

<style scoped>

th {
  text-align: center;
  padding: 15px;
  font-size: 1.2em;
  background-color: #1565c0;
  color: #FFFFFF;
}

.balancesheet td:nth-of-type(2) ~ td {
  min-width: 115px;
  text-align: right;
  font-size: 0.9em;
  font-family: Menlo, Consolas, Monaco, "Lucida Console", monospace;
}

.subtotal {
  font-weight: bold;
  background-color: #bbdefb;
}

.balancesheet .line-label {
  text-align: left;
  font-family: sans-serif;
}

.bs_dif {
  margin-left: 20px;
}

.balance-sheet-icon-col {
  text-align: center;
  width: 50px;
}

.nounderline {
  text-decoration: none !important;
}
</style>