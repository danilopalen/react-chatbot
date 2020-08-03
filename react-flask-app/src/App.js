import React, {useState, useEffect} from 'react';
import './App.css';
//import DetailList from './components/DetailList.js';
//import DetailForm from './components/DetailForm.js';
import Input from './components/Input.js';
import Loader from './components/Loader.js';

function App() {

  //const [details, setDetails] = useState([]);
  const [flow, setFlow] = useState([]);
  const [hasOption, setHasOption] = useState(false);
  /*
  useEffect(() => {
    fetch('/details').then(res => res.json()).then(data => {
      setDetails(data.details);
    });
  }, []);  
  */

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
            console.log("resp", resp)
        
            resp.output.output.generic.forEach(item => {
                if (item.text){
                    let msg = { 'message': item.text}
                    newMessage(msg)
                    setHasOption(false)
                }
                if (item.options) {
                    setHasOption(true)
                    item.options.forEach(option => {
                        let opt = { 'options' : option.label}
                        newOptions(opt);
                    });
                }
            });
        })
    })
  }

  const newMessage = newMessage => setFlow(prev => [...prev, newMessage])

  const newOptions = newOptions => setFlow(prev => [...prev, newOptions])

    return (
      <div className = "container">
        <div className="App" >
          <Loader flow = {flow} submit = {submit} />
        </div>
          <Input submit = {submit} hasOption = {hasOption}/>
        </div>
  );
}

export default App;
