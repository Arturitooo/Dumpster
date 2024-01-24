import { useState } from 'react';
import Alert from './components/Alert';
import { Button } from './components/button';

function App(){
  const [alertVisible, setAlertVisibility] = useState(false);
  return (
  <div>
    { alertVisible && <Alert onClose={() => setAlertVisibility(false)}>My alert</Alert>} 
    <Button color='danger' onClick={()=>setAlertVisibility(true)}>My button</Button>
  </div>)
}

export default App;