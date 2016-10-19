import React from 'react';

const BalanceSheetComponent = ({ LineItems, Differences }) => ( 
    <table className="table table-hover table-condensed table-bordered balancesheet">
        <thead>
            <th className="heading"></th>
            <th className="heading">Local</th>
            <th className="heading">Tax</th>
            <th className="heading">Differenz</th>
            <th className="heading">Matching</th>
            <th className="heading">Gewinnauswirkung</th>
        </thead>
        
            {LineItems.map(item =>
            <tbody>
                <tr key={item.id}>
                    <th className="line-label">{item.name}</th>
                    <th></th>
                    <th></th>
                    <th>{item.subtotal_difference}</th>
                    <th>{item.subtotal_pl_true_up}</th>
                    <th>{item.subtotal_pl_movement}</th>
                </tr>
                {Differences.filter((x) => {return x.bs_line_item_id === item.id}).map(dif =>
                    <tr key={dif.id}>
                        <td className="line-label">{dif.name}</td>
                        <td>{dif.local_gaap}</td>
                        <td>{dif.tax_gaap}</td>
                        <td>{dif.difference}</td>
                        <td>{dif.pl_true_up}</td>
                        <td>{dif.pl_movement}</td>
                    </tr>
                )}
            </tbody>
            )}
    </table>
);

export default BalanceSheetComponent;



