import React, { useState } from 'react';
import { InitialForm } from "./components/InitialForm";
import { RandomImage } from './components/RandomImage';
import Button from '@mui/material/Button';

function App() {
  const [timePerPhoto, setTimePerPhoto] = useState('');
  const [selectedRoot, setSelectedRoot] = useState('');

  const handleBackClick = () => {
    // Reset the timePerPhoto and selectedRoot states to empty strings
    setTimePerPhoto('');
    setSelectedRoot('');
  };

  return (
    <div className="app">
      <div style={{display: 'flex', justifyContent: 'center', alignItems:'center'}}>
        {timePerPhoto !== '' && (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', position: 'absolute', top: '15px', left: '25px' }}>
            <Button variant="text" onClick={handleBackClick}>&lt; Back</Button>
          </div>
        )}
        <h3 style={{textAlign:'center'}}>Niutah assets!</h3> 
      </div>
      <div style={{width:"100%", height:"2px", backgroundColor:"black", opacity:"0.2"}}></div>
      {timePerPhoto === '' ? (
        <InitialForm setTimePerPhoto={setTimePerPhoto} setSelectedRoot={setSelectedRoot} />
      ) : (
        <RandomImage timePerPhoto={timePerPhoto} selectedRoot={selectedRoot} />
      )}
    </div>
  );
}

export default App;
