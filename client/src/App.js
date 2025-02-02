// /src/App.js

import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Login from './components/Login'; // Login component
import Dashboard from './components/Dashboard'; // Dashboard component
import WorkoutPlan from './components/WorkoutPlan'; // Workout plan component

function App() {
  return (
    <div className="App">
      <h1>Workout Planner</h1>
      <Switch>
        <Route exact path="/" component={Login} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/workout-plan" component={WorkoutPlan} />
      </Switch>
    </div>
  );
}

export default App;
