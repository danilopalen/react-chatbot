import React, {useState, useEffect} from 'react';
import './App.css';
import DetailList from './components/DetailList.js';
import DetailForm from './components/DetailForm.js';
import Input from './components/Input.js';
import Response from './components/Response.js';
import Loader from './components/Loader.js';

function App() {

  const [details, setDetails] = useState([]);
  const [flow, setFlow] = useState([]);

  useEffect(() => {
    fetch('/details').then(res => res.json()).then(data => {
      setDetails(data.details);
    });
  }, []);  
  
  return (
      <div className = "container">
        <div className="App">
          <Loader flow = {flow} setFlow = {setFlow}/>
        </div>
          <Input newMessage = {newMessage => setFlow(prev => [...prev, newMessage])}
          newOptions = {newOptions => setFlow(prev => [...prev, newOptions])}/>
      </div>
  );
}

export default App;
