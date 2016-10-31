import Vue from 'vue'
import * as types from './mutation-types'

export default {
    updateDifference: ({ commit }, payload) => {
        let data = {
            id: payload.formData.id,
            comment: payload.formData.comment,
            local_gaap: (parseFloat(payload.formData.local_gaap) || 0).toFixed(2),
            tax_gaap: (parseFloat(payload.formData.tax_gaap) || 0).toFixed(2),
            pl_permanent: (parseFloat(payload.formData.pl_permanent) || 0).toFixed(2),
            oci_permanent: (parseFloat(payload.formData.oci_permanent) || 0).toFixed(2),
            oci_temporary: (parseFloat(payload.formData.oci_temporary) || 0).toFixed(2)
        }
        
        commit(types.STATUS_START)
        
        Vue.http.put(providedDetailURL + payload.formData.id, data)
        .then((response) => {
            payload['response'] = response.body
            commit(types.UPDATE_DIFFERENCE, payload)
            commit(types.STATUS_FINISH)
        }, (response) => {
            console.log("ERROR", response)
            // TODO: Error-Handling in Details-View (Backend currently rises BadRequest400 with error as short string description)
            commit(types.STATUS_FINISH)
        })        
    }
}