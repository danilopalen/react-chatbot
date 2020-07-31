import React from 'react';

class DetailList extends React.Component {
    render() {
        const {list} = this.props;

        return (
            <>
            <div>{list.email}</div>
            </>
        )        
    }
}
export default DetailList;