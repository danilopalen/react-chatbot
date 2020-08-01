import React from 'react';

class Response extends React.Component {
    render() {
        const {res} = this.props;

        if (res.options) {
            return (
                <div>
                    <h3>{res.message}</h3>
                    <button value = {res.options}>{res.options}</button>
                </div>
            )
        }else{
            return (
                <div>
                    <h3>{res.message}</h3>
                </div>
            )
        }       
    }
}
export default Response;