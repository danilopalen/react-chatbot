import React from 'react'
import '.././App.css';

class  Input extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            text : '',
        }
    }
    componentDidMount(){
        this.submit();
    }

    submit(){
        const url = "/input";
        let data = this.state;

        fetch(url, {
            method: 'POST',
            headers: {
                "Content-Type" : "application/json",
                "Accept" : "application/json"
            },
            body: JSON.stringify(data)
        }).then((result) => {
            result.json().then((resp) => {
                console.log("resp", resp)

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
        this.setState({
            text: '',
        })
    }
    render() { 
        return ( 
            <div className = 'input-group mb-3 container' style = {{position: 'absolute',
                bottom: '10%', marginLeft: '-12px'}}>

                <input className = 'form-control' type = 'text' value = {this.state.text} name = 'text' placeholder = 'Enter message'
                onChange = {e => this.setState({text : e.target.value})}></input><br/>
                
                <div class="input-group-append">
                    <span class="input-group-text" onClick = {() => {this.submit()}}>Send</span>
                </div>
            </div>
        );
        
    }
}
 
export default Input;