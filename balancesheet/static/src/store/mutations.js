//
// Initial Data for Development without a backend. 
// To be deleted once the Vue-App is running as static file from the backend
//
// Dummy-Data BEGIN
//

//let providedData = {
//  Differences: [
//    {pl_movement: -1000.00, py_difference: 0.00, tu_permanent: 0.00, difference: -1000.00, tu_pl_temporary: 0.00, py_temporary: 0.00, py_oci: 0.00, py_local_gaap: 0.00, tu_difference: 0.00, version_id: 1, py_pl_temporary: 0.00, local_gaap: 1000.00, pl_true_up: 0.00, pl_temporary: -1000.00, tu_pl_permanent: 0.00, tu_temporary: 0.00, py_pl_permanent: 0.00, tu_oci_temporary: 0.00, oci_temporary: 0.00, pl_permanent: 0.00, oci: 0.00, tu_tax_gaap: 0.00, oci_permanent: 0.00, py_oci_temporary: 0.00, tax_gaap: 0.00, tu_oci: 0.00, tu_oci_permanent: 0.00, py_permanent: 0.00, permanent: 0.00, name: 'Abweichende Aktivierung Firmenwert', bs_line_item_id: 1, tu_local_gaap: 0.00, id: 1, temporary: -1000.00, py_tax_gaap: 0.00, py_oci_permanent: 0.00, comment: ''}
//  ],
//  LineItems: [
//    {subtotal_pl_true_up: 0.00, name: 'U81000 - Goodwill', subtotal_temporary: -1000.00, id: 1, subtotal_pl_movement: -1000.00, sorting: 1, subtotal_difference: -1000.00}, 
//    {subtotal_pl_true_up: null, name: 'U81010 - VBI', subtotal_temporary: null, id: 2, subtotal_pl_movement: null, sorting: 2, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81020 - Deferred acquisition costs', subtotal_temporary: null, id: 3, subtotal_pl_movement: null, sorting: 3, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81030 - Other intangible assets', subtotal_temporary: null, id: 4, subtotal_pl_movement: null, sorting: 4, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81040 - Investments in real estate properties', subtotal_temporary: null, id: 5, subtotal_pl_movement: null, sorting: 5, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81050 - Invested financial assets (including assets backing UL and excluding investments in real estate properties)', subtotal_temporary: null, id: 6, subtotal_pl_movement: null, sorting: 6, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81060 - Other tangible assets', subtotal_temporary: null, id: 7, subtotal_pl_movement: null, sorting: 7, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81070 - Technical reserves (including reinsurance)', subtotal_temporary: null, id: 8, subtotal_pl_movement: null, sorting: 8, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81080 - Pensions and other retirement benefits', subtotal_temporary: null, id: 9, subtotal_pl_movement: null, sorting: 9, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81090 - Employee benefits (other than Pensions)', subtotal_temporary: null, id: 10, subtotal_pl_movement: null, sorting: 10, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81100 - Other provisions for risk and other charges', subtotal_temporary: null, id: 11, subtotal_pl_movement: null, sorting: 11, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81120 - Other assets', subtotal_temporary: null, id: 12, subtotal_pl_movement: null, sorting: 13, subtotal_difference: null}, 
//    {subtotal_pl_true_up: null, name: 'U81130 - Other liabilities', subtotal_temporary: null, id: 13, subtotal_pl_movement: null, sorting: 14, subtotal_difference: null}
//    ]
//}

//if (typeof providedDifferences!=='undefined') {
//  providedData = {
//    Differences: providedDifferences,
//    LineItems: providedLineItems
//  }
//}

//
// Dummy-Data END
//

// Definition of STATE


export const state = {
    Differences: providedDifferences,
    LineItems: providedLineItems,
    Status: 0
    }

// Definition of MUTATIONS

import * as types from './mutation-types'

export const mutations = {
    [types.UPDATE_DIFFERENCE] (state, payload) {
      
      // Update the current difference (which is connected and updates the store) 
      // with the response values. Result: Store is up-to-date, Balance Sheet List-
      // view reflects the new data.
      Object.assign(payload.difference, JSON.parse(payload.response.difference))
      
      // Problem: The currently visible single difference is not the difference
      // from the store (not connected) but just a copy of the difference. In order
      // to display the response-data in the currently visible difference-form,
      // the updated difference (see command above) needs to update the formData
      // which represents what the user sees in the Difference-Update-Form.
      // Object.assign(payload.formData, JSON.parse(payload.response.difference))
      Object.assign(payload.formData, payload.difference)
    },
    [types.STATUS_START] (state) {
      state.Status++
    },
    [types.STATUS_FINISH] (state) {
      state.Status--
    }
}