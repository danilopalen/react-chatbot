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
        this.props.submit(this.state.text);
    }
    
    render() { 
        return ( 
            <div className = 'input-group mb-3 container' style = {{position: 'absolute',
                bottom: '10%', marginLeft: '-12px'}}>

                <input className = 'form-control' type = 'text' name = 'text' placeholder = 'Enter message'
                onChange = {e => this.setState({text : e.target.value})}
                disabled = {this.props.hasOption}
                ></input><br/>
                
                <div class="input-group-append">
                    <button class="input-group-text" disabled = {this.props.hasOption} onClick = {() => {this.props.submit(this.state.text)}}>Send</button>
                </div>
            </div>
        );
        
    }
}
 
export default Input;