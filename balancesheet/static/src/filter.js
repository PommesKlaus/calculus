

export const num = function(value) {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}