// /src/contexts/AuthContext.js

import React, { createContext, useState, useContext } from 'react';

// Create the AuthContext
const AuthContext = createContext();

// Custom hook to use AuthContext
export const useAuth = () => useContext(AuthContext);

// AuthProvider component to provide authentication context
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // User state

  const login = (username, password) => {
    // Perform login logic, set user in state
    setUser({ username });
  };

  const logout = () => {
    // Perform logout logic, reset user state
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
