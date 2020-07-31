import React, {useState, useEffect} from 'react';
import './App.css';
import DetailList from './components/DetailList.js';
import DetailForm from './components/DetailForm.js';
import Input from './components/Input.js';
import Response from './components/Response.js';


function App() {

  const [details, setDetails] = useState([]);
  const [flow, setFlow] = useState([]);

  useEffect(() => {
    fetch('/details').then(res => res.json()).then(data => {
      setDetails(data.details);
    });
  }, []);  

  return (
      <div className="App">
        {flow.map(res => <Response res = {res} key = {res.id}/>)}
        <br></br>
        <Input newMessage = {newMessage => setFlow(prev => [...prev, newMessage])}
        newOptions = {newOptions => setFlow(prev => [...prev, newOptions])}/>
        <br></br>
        <DetailForm />
        <h2>List of saved email from Database</h2>
        {details.map(details => <DetailList list = {details} key = {details.id}/>)}    
      </div>
  );
}

export default App;
