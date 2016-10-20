import React from 'react';

const BalanceSheetComponent = ({ LineItems, Differences }) => ( 
    <table className="table table-hover table-condensed table-bordered balancesheet">
        <thead>
            <tr>
                <th></th>
                <th>Local</th>
                <th>Tax</th>
                <th>Differenz</th>
                <th>Matching</th>
                <th>Gewinn</th>
            </tr>
        </thead>
        
            {LineItems.map(item =>
            <tbody>
                <tr key={item.id}>
                    <td className="line-label subtotal">{item.name}</td>
                    <td className="subtotal"></td>
                    <td className="subtotal"></td>
                    <td className="subtotal">{item.subtotal_difference}</td>
                    <td className="subtotal">{item.subtotal_pl_true_up}</td>
                    <td className="subtotal">{item.subtotal_pl_movement}</td>
                </tr>
                {Differences.filter((x) => {return x.bs_line_item_id === item.id}).map(dif =>
                    <tr key={dif.id}>
                        <td className="line-label"><div className="bs_dif">{dif.name}</div></td>
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



