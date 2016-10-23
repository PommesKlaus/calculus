import { connect } from 'react-redux';
import AddDifferenceComponent from '../components/AddDifferenceComponent';
import {hideAddDifferenceModal} from '../actions';

const mapStateToProps = (state) => {
    return({
        LineItems: state.LineItems,
        AddToLineItem: state.AddToLineItem
    })
};

const mapDispatchToProps = (dispatch) => {
  return {
    hideModal: () => {
      dispatch(hideAddDifferenceModal());
    }
  }
}

const AddDifferenceContainer = connect(mapStateToProps, mapDispatchToProps)(AddDifferenceComponent);

export default AddDifferenceContainer;