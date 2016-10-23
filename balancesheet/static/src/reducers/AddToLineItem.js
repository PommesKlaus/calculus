const AddToLineItem = (state=null, action) => {
    switch (action.type) {
        case "SHOW_ADD_DIFFERENCE_MODAL":
            return action.id;
        case "HIDE_ADD_DIFFERENCE_MODAL":
            return null;
        default:
            return state;
    }
};

export default AddToLineItem;