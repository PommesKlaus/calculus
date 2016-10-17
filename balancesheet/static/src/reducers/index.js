import { combineReducers } from 'redux';
import LineItems from  './LineItems';
import Differences from './Differences';

const App = combineReducers({
    LineItems,
    Differences
});

export default App;