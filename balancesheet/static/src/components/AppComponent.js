import React from 'react';
import LineItemsContainer from '../containers/LineItemsContainer';

class App extends React.Component {
    render() {
        return (
            <div className="container">
                <h1>Bilanz</h1>
                <table className="table table-hover table-condensed">
                    <thead>
                    <tr>
                        <th className="col-xs-7"></th>
                        <th className="col-xs-1">Local</th>
                        <th className="col-xs-1">TAX</th>
                        <th className="col-xs-1">Differenz</th>
                        <th className="col-xs-1">Matching</th>
                        <th className="col-xs-1">Gewinnauswirkung</th>
                    </tr>
                    </thead>
                    <LineItemsContainer />
                </table>
            </div>);
    }
}

export default App;