import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Dashboard from "./components/Dashboard";
import ThemeSwitcher from "./components/ThemeSwitcher";
import './App.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div>
          <ThemeSwitcher />
          <Switch>
            <Route path="/login" component={Login} />
            <Route path="/signup" component={Signup} />
            <Route path="/dashboard" component={Dashboard} />
            <Route path="/" exact>
              <h2>Welcome to the Workout Planner</h2>
            </Route>
          </Switch>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
