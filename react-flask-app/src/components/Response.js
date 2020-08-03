import React from 'react';
import '.././App.css';

class Response extends React.Component {
    render() {
        const {res, submit} = this.props;

        

        if (res.options) {
            return (
                <div className = 'btn-group'>
                    <button className = 'btn btn-info'  value = {res.options} onClick = {(e) => {submit(e.target.value)}} >{res.options}</button>
                </div>
            );
        }else{
            return (
                <h3 style = {{backgroundColor: '#fff', 
                marginTop: '20px',
                padding: '20px'
                }}>{res.message}</h3>
            );
        }       
    }
}
export default Response;