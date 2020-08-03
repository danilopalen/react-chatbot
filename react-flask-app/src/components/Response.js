import React from 'react';
import '.././App.css';

class Response extends React.Component {
    render() {
        const {res, newMessage, newOptions} = this.props;

        const submit = (data) => {
            const url = "/input";

            fetch(url, {
                method: 'POST',
                headers: {
                    "Content-Type" : "application/json",
                    "Accept" : "application/json"
                },
                body: JSON.stringify({text : data})
            }).then((result) => {
                result.json().then((resp) => {
                    console.warn("resp", resp)
                
                    resp.output.output.generic.forEach(item => {
                        if (item.text){
                            let msg = { 'message': item.text}
                            this.props.newMessage(msg)
                        }
                        if (item.options) {
                            item.options.forEach(option => {
                                let opt = { 'options' : option.label}
                                return this.props.newOptions(opt);
                            });
                        }
                    });
                })
            })
        }

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