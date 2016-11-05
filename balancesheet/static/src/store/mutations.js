// Definition of STATE


export const state = {
    Differences: providedDifferences,
    LineItems: providedLineItems,
    Totals: providedTotals,
    Version: providedVersion,
    Status: 0
    }

// Definition of MUTATIONS

import * as types from './mutation-types'

export const mutations = {
    [types.UPDATE_DIFFERENCE] (state, payload) {
      
      // Update the current difference (which is connected and updates the store) 
      // with the response values. Result: Store is up-to-date, Balance Sheet List-
      // view reflects the new data.
      Object.assign(payload.difference, payload.response.difference)
      Object.assign(payload.lineItem, payload.response.lineItem)
      
      // Problem: The currently visible single difference is not the difference
      // from the store (not connected) but just a copy of the difference. In order
      // to display the response-data in the currently visible difference-form,
      // the updated difference (see command above) needs to update the formData
      // which represents what the user sees in the Difference-Update-Form.
      // Object.assign(payload.formData, JSON.parse(payload.response.difference))
      Object.assign(payload.formData, payload.difference)
    },
    
    [types.NEW_DIFFERENCE] (state, payload) {
      state.Differences.push(payload.response.difference)
      Object.assign(payload.lineItem, payload.response.lineItem)
      Object.assign(payload.totals, payload.response.totals)
    },

    [types.DELETE_DIFFERENCE] (state, payload) {
      for(let i=0; i<= state.Differences.length; i++) {
        if (state.Differences[i].id===payload.difference.id) {
          state.Differences.splice( i, 1 );
        }
      }
    },
    
    [types.STATUS_START] (state) {
      state.Status++
    },
    
    [types.STATUS_FINISH] (state) {
      state.Status--
    }
}