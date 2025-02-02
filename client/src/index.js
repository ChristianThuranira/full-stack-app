// /src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css'; // Global styles
import App from './App';      // Main app component
import { BrowserRouter as Router } from 'react-router-dom'; // For routing
import { AuthProvider } from './contexts/AuthContext'; // For auth context

// Rendering the app and wrapping it with providers
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
