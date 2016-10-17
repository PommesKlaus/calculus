import React from 'react';
import Differences from '../containers/DifferencesContainer';

const LineItemsComponent = ({ LineItems }) => (
    <div>
        {LineItems.map(item =>
            <div key={item.id}>
                <strong key={item.id}>{item.name}</strong>
                <Differences LineItemId={item.id} />
            </div>
        )}
    </div>
);

export default LineItemsComponent;