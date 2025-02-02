// /src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css'; // Import global styles
import App from './App';      // Import the main app component
import { BrowserRouter as Router } from 'react-router-dom'; // For routing
import { AuthProvider } from './contexts/AuthContext'; // For auth context

// Render the App component wrapped with necessary providers (auth and routing)
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
