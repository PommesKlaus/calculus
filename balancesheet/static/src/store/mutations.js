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