import React from 'react';
import ReactDOM from 'react-dom';
import { applyMiddleware, createStore } from 'redux';
import { Provider } from 'react-redux';
import App from './components/AppComponent';
import combinedReducer from './reducers/index'
import createLogger from 'redux-logger';


const logger = createLogger();

const store = createStore(combinedReducer, applyMiddleware(logger));

ReactDOM.render(
    (
        <Provider store={store}>
          <App />
        </Provider>
    ), document.getElementById('root'));