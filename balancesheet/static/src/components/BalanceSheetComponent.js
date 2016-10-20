import React from 'react';
import Numeral from 'numeral';
import language from 'numeral/min/languages.min';

Numeral.language('de', {
    delimiters: {
        thousands: '.',
        decimal: ','
    },
    abbreviations: {
        thousand: 'k',
        million: 'm',
        billion: 'b',
        trillion: 't'
    },
    ordinal: function (number) {
        return '.';
    },
    currency: {
        symbol: '€'
    }
});
Numeral.language('de');

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
                    <td className="subtotal">{Numeral(item.subtotal_difference).format('0,0.00')}</td>
                    <td className="subtotal">{Numeral(item.subtotal_pl_true_up).format('0,0.00')}</td>
                    <td className="subtotal">{Numeral(item.subtotal_pl_movement).format('0,0.00')}</td>
                </tr>
                {Differences.filter((x) => {return x.bs_line_item_id === item.id}).map(dif =>
                    <tr key={dif.id}>
                        <td className="line-label"><div className="bs_dif">{dif.name}</div></td>
                        <td>{Numeral(dif.local_gaap).format('0,0.00')}</td>
                        <td>{Numeral(dif.tax_gaap).format('0,0.00')}</td>
                        <td>{Numeral(dif.difference).format('0,0.00')}</td>
                        <td>{Numeral(dif.pl_true_up).format('0,0.00')}</td>
                        <td>{Numeral(dif.pl_movement).format('0,0.00')}</td>
                    </tr>
                )}
            </tbody>
            )}
    </table>
);

export default BalanceSheetComponent;



