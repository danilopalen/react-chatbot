import React from 'react';
import '.././App.css';
import Response from './Response.js';

class Loader extends React.Component {
    render() {
        const {flow, setFlow} = this.props;
        if (flow.length > 0 ){
            return (
                <>{flow.map(res => <Response res = {res} newMessage = {newMessage => setFlow(prev => [...prev, newMessage])}
                newOptions = {newOptions => setFlow(prev => [...prev, newOptions])} />)}</>
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