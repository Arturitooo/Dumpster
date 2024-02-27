import './App.css';
import {Routes, Route, Router} from 'react-router-dom';
import { Home } from './components/Home';
import { About } from './components/About';
import { Create } from './components/Create';
import { Navbar } from './components/Navbar';


function App() {
  const navbarWidth = 240;
  return (
    <div className="App">
      <Navbar 
        drawerWidth={navbarWidth}
        content = {
          <Routes>
            <Route path="" element={<Home/>} />
            <Route path="/about" element={<About/>} />
            <Route path="/create" element={<Create/>} />
          </Routes>
        }
      />
    </div>
  );
}

export default App;
