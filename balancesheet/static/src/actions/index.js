
export const add_todo = (text) => {
    return ({
        type: "ADD_TODO",
        id: nextTodoId++,
        text: text
    })
};

export const deleteTodo = (id) => {
    return ({
        type: "DELETE_TODO",
        id: id
    });
};