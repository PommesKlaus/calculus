import React from 'react';

const DifferencesComponent = ({ props, Differences }) => (
    <ul>
        {Differences.filter((item) => {return item.bs_line_item_id === props.LineItemId})
        .map(dif =>
            <div key={dif.id}>
                <span key={dif.id}>{dif.name}</span>
            </div>

        )}
    </ul>
);

export default DifferencesComponent;