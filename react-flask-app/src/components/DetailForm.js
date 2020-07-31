import React from 'react'

class DetailForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            id : '',
            fname : '',
            lname : '',
            email : ''
         }
    }
    submit(){
        const url = "/add_details";
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
            })
        })
        this.setState({
            id : '',
            fname : '',
            lname : '',
            email : ''
        })
    }
    render() { 
        return ( 
            <div>
                <input type = 'text' value = {this.state.id} name = 'id' placeholder = 'Id'
                onChange = {e => this.setState({id : e.target.value})}></input><br/>
                <input type = 'text' value = {this.state.fname} name = 'fname' placeholder = 'Firstname'
                onChange = {e => this.setState({fname : e.target.value})}></input><br/>
                <input type = 'text' value = {this.state.lname} name = 'lname' placeholder = 'Lastname'
                onChange = {e => this.setState({lname : e.target.value})}></input><br/>
                <input type = 'text' value = {this.state.email} name = 'email' placeholder = 'Email'
                onChange = {e => this.setState({email : e.target.value})}></input><br/>
                <button onClick = {() => {this.submit()}}>Submit</button>
            </div>            
        );
    }
}
 
export default DetailForm;