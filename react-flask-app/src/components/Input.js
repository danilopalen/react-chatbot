import React from 'react'

class  Input extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            message_type: 'text',
            text: ''  
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
                console.warn("resp", resp)
                let msg = { 'message': resp.response}
                this.props.newMessage(msg)
                if ( resp.output.output.generic.length === 2){
                    resp.output.output.generic[1].options.map(d => {
                        console.log(d);
                        let opt = { 'options' : d.label}
                        return this.props.newOptions(opt);
                    })
                }else{
                    this.props.newOptions(' ');
                }
                
            })
        })
        this.setState({
            text: '',
        })
    }
    render() { 
        return ( 
            <div>
                <input type = 'text' value = {this.state.text} name = 'text' placeholder = 'Enter message'
                onChange = {e => this.setState({text : e.target.value})}></input><br/>
                <button onClick = {() => {this.submit()}}>Submit</button>
            </div>
         );
    }
}
 
export default Input;