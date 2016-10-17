import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import App from './components/AppComponent';
import combinedReducer from './reducers/index'

const store = createStore(combinedReducer);

ReactDOM.render(
    (
        <Provider store={store}>
          <App />
        </Provider>
    ), document.getElementById('root'));