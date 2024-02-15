import { InitialForm } from "./components/InitialForm/InitialForm";

function App() {
  return (
    <div className="app">
      <h1 style={{textAlign:'center'}}>Niutah assets!</h1>
      <div style={{width:"100%", height:"2px", backgroundColor:"black", opacity:"0.2"}}></div>
      <InitialForm/>
    </div>
  );
}

export default App;
