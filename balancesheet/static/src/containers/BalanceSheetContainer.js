import { connect } from 'react-redux';
import BalanceSheetComponent from '../components/BalanceSheetComponent';
import {showAddDifferenceModal} from '../actions';

const mapStateToProps = (state) => {
    return({
        LineItems: state.LineItems,
        Differences: state.Differences
    })
};

const mapDispatchToProps = (dispatch) => {
  return {
    showAddDifferenceModal: (id) => {
      dispatch(showAddDifferenceModal(id))
    }
  }
}

const BalanceSheetContainer = connect(mapStateToProps, mapDispatchToProps)(BalanceSheetComponent);

export default BalanceSheetContainer;