<template>
  <div>
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
          <td class="line-label"><div class="bs_dif">{{ dif.name }}</div></td>
          <td>{{ dif.local_gaap }}</td>
          <td>{{ dif.tax_gaap }}</td>
          <td>{{ dif.difference }}</td>
          <td>{{ dif.pl_true_up }}</td>
          <td>{{ dif.pl_movement }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
let dummyData = {
  Differences: [
    {pl_movement: -1000.00, py_difference: 0.00, tu_permanent: 0.00, difference: -1000.00, tu_pl_temporary: 0.00, py_temporary: 0.00, py_oci: 0.00, py_local_gaap: 0.00, tu_difference: 0.00, version_id: 1, py_pl_temporary: 0.00, local_gaap: 1000.00, pl_true_up: 0.00, pl_temporary: -1000.00, tu_pl_permanent: 0.00, tu_temporary: 0.00, py_pl_permanent: 0.00, tu_oci_temporary: 0.00, oci_temporary: 0.00, pl_permanent: 0.00, oci: 0.00, tu_tax_gaap: 0.00, oci_permanent: 0.00, py_oci_temporary: 0.00, tax_gaap: 0.00, tu_oci: 0.00, tu_oci_permanent: 0.00, py_permanent: 0.00, permanent: 0.00, name: 'Abweichende Aktivierung Firmenwert', bs_line_item_id: 1, tu_local_gaap: 0.00, id: 1, temporary: -1000.00, py_tax_gaap: 0.00, py_oci_permanent: 0.00, comment: ''}
  ],
  LineItems: [
    {subtotal_pl_true_up: 0.00, name: 'U81000 - Goodwill', subtotal_temporary: -1000.00, id: 1, subtotal_pl_movement: -1000.00, sorting: 1, subtotal_difference: -1000.00}, 
    {subtotal_pl_true_up: null, name: 'U81010 - VBI', subtotal_temporary: null, id: 2, subtotal_pl_movement: null, sorting: 2, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81020 - Deferred acquisition costs', subtotal_temporary: null, id: 3, subtotal_pl_movement: null, sorting: 3, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81030 - Other intangible assets', subtotal_temporary: null, id: 4, subtotal_pl_movement: null, sorting: 4, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81040 - Investments in real estate properties', subtotal_temporary: null, id: 5, subtotal_pl_movement: null, sorting: 5, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81050 - Invested financial assets (including assets backing UL and excluding investments in real estate properties)', subtotal_temporary: null, id: 6, subtotal_pl_movement: null, sorting: 6, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81060 - Other tangible assets', subtotal_temporary: null, id: 7, subtotal_pl_movement: null, sorting: 7, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81070 - Technical reserves (including reinsurance)', subtotal_temporary: null, id: 8, subtotal_pl_movement: null, sorting: 8, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81080 - Pensions and other retirement benefits', subtotal_temporary: null, id: 9, subtotal_pl_movement: null, sorting: 9, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81090 - Employee benefits (other than Pensions)', subtotal_temporary: null, id: 10, subtotal_pl_movement: null, sorting: 10, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81100 - Other provisions for risk and other charges', subtotal_temporary: null, id: 11, subtotal_pl_movement: null, sorting: 11, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81120 - Other assets', subtotal_temporary: null, id: 12, subtotal_pl_movement: null, sorting: 13, subtotal_difference: null}, 
    {subtotal_pl_true_up: null, name: 'U81130 - Other liabilities', subtotal_temporary: null, id: 13, subtotal_pl_movement: null, sorting: 14, subtotal_difference: null}
    ]
}

let providedData = {}
if (typeof providedDifferences!=='undefined') {
  providedData = {
    Differences: providedDifferences,
    LineItems: providedLineItems
  }
}

module.exports = {
  data: function() {
    return dummyData
  },
  methods:  {
    filteredDifferences: function(lineItemId, differences) {
      return differences.filter(function (x) {
        return x.bs_line_item_id === lineItemId;
      });
    }
  }
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