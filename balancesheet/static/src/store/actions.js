import Vue from 'vue'
import * as types from './mutation-types'
import router from '../routes'

export default {
    updateDifference: ({ commit }, payload) => {
        let data = {
            id: payload.formData.id,
            comment: payload.formData.comment,
            local_gaap: payload.formData.local_gaap,
            tax_gaap: payload.formData.tax_gaap,
            pl_permanent: payload.formData.pl_permanent,
            oci_permanent: payload.formData.oci_permanent,
            oci_temporary: payload.formData.oci_temporary
        }
        
        commit(types.STATUS_START)
        
        Vue.http.put(providedDetailURL + payload.formData.id, data)
        .then((response) => {
            payload['response'] = {}
            payload['response']['difference'] = JSON.parse(response.body.difference)
            payload['response']['lineItem'] = JSON.parse(response.body.line_item)
            payload['response']['totals'] = JSON.parse(response.body.totals)
            commit(types.UPDATE_DIFFERENCE, payload)
            commit(types.STATUS_FINISH)
        }, (response) => {
            console.log("ERROR", response)
            // TODO: Error-Handling in Details-View (Backend currently rises BadRequest400 with error as short string description)
            commit(types.STATUS_FINISH)
        })        
    },
    
    newDifference: ({ commit }, payload) => {
        let data = {
            name: payload.formData.name,
            bs_line_item_id: payload.formData.bs_line_item_id,
            version_id: payload.formData.version_id,
            comment: payload.formData.comment,
            local_gaap: payload.formData.local_gaap,
            tax_gaap: payload.formData.tax_gaap,
            pl_permanent: payload.formData.pl_permanent,
            oci_permanent: payload.formData.oci_permanent,
            oci_temporary: payload.formData.oci_temporary
        }
        
        commit(types.STATUS_START)
        Vue.http.post(providedDetailURL, data)
        .then((response) => {
            payload['response'] = {}
            payload['response']['difference'] = JSON.parse(response.body.difference)
            payload['response']['lineItem'] = JSON.parse(response.body.line_item)
            payload['response']['totals'] = JSON.parse(response.body.totals)
            commit(types.NEW_DIFFERENCE, payload)
            commit(types.STATUS_FINISH)
            router.push({ name: 'differenceDetails', params: { differenceId: payload.response.difference.id }})
        }, (response) => {
            console.log("ERROR", response)
            // TODO: Error-Handling in Details-View (Backend currently rises BadRequest400 with error as short string description)
            commit(types.STATUS_FINISH)
        })        
    },

    deleteDifference: ({ commit }, payload) => {
        
        commit(types.STATUS_START)       
        Vue.http.delete(providedDetailURL + payload.difference.id, {id: payload.difference.id})
        .then((response) => {
            commit(types.DELETE_DIFFERENCE, payload)
            commit(types.STATUS_FINISH)
            router.push({ name: 'BalanceSheet'})
        }, (response) => {
            console.log("ERROR", response)
            // TODO: Error-Handling in Details-View (Backend currently rises BadRequest400 with error as short string description)
            commit(types.STATUS_FINISH)
        })        
    }
}