import React, { useState } from 'react';
import { InitialForm } from "./components/InitialForm";
import { Timer } from "./components/Timer";

function App() {
  const [timePerPhoto, setTimePerPhoto] = useState('');

  return (
    <div className="app">
      <div style={{display: 'flex', justifyContent: 'center', alignItems:'center'}}>
        <h1 style={{textAlign:'center'}}>Niutah assets!</h1> 
        {timePerPhoto && <Timer timePerPhoto={timePerPhoto} />}
      </div>
      <div style={{width:"100%", height:"2px", backgroundColor:"black", opacity:"0.2"}}></div>
      {timePerPhoto === '' ? (
        <InitialForm setTimePerPhoto={setTimePerPhoto} />
      ) : (
        <Timer timePerPhoto={timePerPhoto} />
      )}
      
    </div>
  );
}

export default App;
