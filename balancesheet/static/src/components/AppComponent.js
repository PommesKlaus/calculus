import React from 'react';
import BalanceSheetContainer from '../containers/BalanceSheetContainer';

class App extends React.Component {
    render() {
        return (
            <div className="container-fluid">
                <h1>Bilanz</h1>
                <BalanceSheetContainer />
            </div>);
    }
}

export default App;