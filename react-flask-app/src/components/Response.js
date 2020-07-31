import React from 'react';

class Response extends React.Component {
    render() {
        const {res} = this.props;

        return (
            <div>
                <div>{res}</div>
            </div>
        )        
    }
}
export default Response;