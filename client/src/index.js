import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Import global styles
import App from './App'; // Import the main App component
import { BrowserRouter as Router } from 'react-router-dom'; // Import React Router for routing
import { AuthProvider } from './contexts/AuthContext'; // Import the AuthProvider for managing authentication state

// Render the app inside the "root" div and wrap it with AuthProvider and Router
ReactDOM.render(
  <React.StrictMode>
    <AuthProvider>
      <Router>
        <App />
      </Router>
    </AuthProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
