
export const showAddDifferenceModal = (id) => {
    return ({
        type: "SHOW_ADD_DIFFERENCE_MODAL",
        id: id
    })
};

export const hideAddDifferenceModal = () => {
    return ({
        type: "HIDE_ADD_DIFFERENCE_MODAL"
    })
};

export const deleteTodo = (id) => {
    return ({
        type: "DELETE_TODO",
        id: id
    });
};