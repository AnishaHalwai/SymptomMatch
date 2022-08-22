import logo from './logo.svg';
import './App.css';
import Home from './Home'
import Diagnose from './Diagnose';
import NavBar from './NavBar'; 
import Predict from './Predict';
import {Routes, Route} from 'react-router-dom';

function App() {
  return (
    <div>
        {/* <Home /> */}
        
        <Routes>
          <Route path ="/" element={<Home/>} />
          <Route path ="/diagnose" element={<Diagnose/>} /> 
          <Route path ="/prediction" element={<Predict/>} /> 

        </Routes>
       
    </div>
  );
}

export default App;
