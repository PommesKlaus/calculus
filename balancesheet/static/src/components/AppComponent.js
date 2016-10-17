import React from 'react';
import LineItemsContainer from '../containers/LineItemsContainer';

class App extends React.Component {
    render() {
        return (
            <div>
                <h1>Bilanz</h1>
                <LineItemsContainer />
            </div>);
    }
}

export default App;