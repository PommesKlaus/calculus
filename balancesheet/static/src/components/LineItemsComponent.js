import React from 'react';
import Differences from '../containers/DifferencesContainer';

const LineItemsComponent = ({ LineItems }) => ( 
    <tbody>
        {LineItems.map(item =>
            <tbody key={item.id}>
            <tr>
                <th className="col-xs-7">{item.name}</th>
                <th className="col-xs-1"></th>
                <th className="col-xs-1"></th>
                <th className="col-xs-1">{item.subtotal_difference}</th>
                <th className="col-xs-1">{item.subtotal_pl_true_up}</th>
                <th className="col-xs-1">{item.subtotal_pl_movement}</th>
            </tr>
            <Differences LineItemId={item.id} />
            </tbody>
        )}
    </tbody>
);

export default LineItemsComponent;