import { combineReducers } from 'redux';
import LineItems from  './LineItems';
import Differences from './Differences';
import AddToLineItem from './AddToLineItem';

const App = combineReducers({
    LineItems,
    Differences,
    AddToLineItem
});

export default App;