import { connect } from 'react-redux';
import LineItemsComponent from '../components/LineItemsComponent';

const mapStateToProps = (state) => {
    return({
        LineItems: state.LineItems,
    })
};

const LineItemsContainer = connect(mapStateToProps)(LineItemsComponent);

export default LineItemsContainer;