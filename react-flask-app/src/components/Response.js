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
                    let msg = { 'message': resp.response}
                    this.props.newMessage(msg)
                    if ( resp.output.output.generic.length === 2){
                        resp.output.output.generic[1].options.map(d => {
                            console.log(d);
                            let opt = { 'options' : d.label}
                            return this.props.newOptions(opt);
                        })
                    }
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