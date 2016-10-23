import React from 'react';
import BalanceSheetContainer from '../containers/BalanceSheetContainer';
import AddDifferenceContainer from '../containers/AddDifferenceContainer';
import { Button } from 'react-bootstrap';

class App extends React.Component {
    render() {
        return (
            <div className="container-fluid">
                <h1>Bilanz</h1>
                <BalanceSheetContainer />
                <AddDifferenceContainer />
            </div>);
    }
}

export default App;