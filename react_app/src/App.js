import './App.css';
import Index from './components/Index'
import Ecuaciones from './components/ecuaciones'
import Regresion from './components/regresion'
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
      <Switch>
        <Route exact path="/" component={Index}/>
        <Route exact path="/ecuaciones" component={Ecuaciones}/>
        <Route exact path="/regresion" component={Regresion}/>
      </Switch>
      </Router>
    </div>
  );
}

export default App;
