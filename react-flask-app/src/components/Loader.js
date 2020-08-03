import React from 'react';
import '.././App.css';
import Response from './Response.js';

class Loader extends React.Component {
    render() {
        const {flow, submit} = this.props;

        if (flow.length > 0 ){
            return (
                <>{flow.map(res => <Response res = {res} submit = {submit} />)}</>
            );
        }else{
            return (
                <><span class="spinner-grow spinner-grow-lg"></span>
                <span class="display-4"> Loading..</span></>
            );
        }   
    }
}
export default Loader;