import { connect } from 'react-redux';
import BalanceSheetComponent from '../components/BalanceSheetComponent';

const mapStateToProps = (state) => {
    return({
        LineItems: state.LineItems,
        Differences: state.Differences
    })
};

const BalanceSheetContainer = connect(mapStateToProps)(BalanceSheetComponent);

export default BalanceSheetContainer;