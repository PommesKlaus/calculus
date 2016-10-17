import { connect } from 'react-redux';
import DifferencesComponent from '../components/DifferencesComponent';


const mapStateToProps = (state, props) => {
    return({
        Differences: state.Differences,
        props: props,
    })
};

const Differences = connect(mapStateToProps)(DifferencesComponent);

export default Differences;