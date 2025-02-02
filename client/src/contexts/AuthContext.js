import { createContext, useState, useEffect } from "react";
import axios from "axios";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("authToken");
    if (token) {
      axios
        .get("http://localhost:5000/api/protected", {
          headers: { "x-auth-token": token },
        })
        .then((response) => {
          setUser(response.data);
        })
        .catch(() => {
          localStorage.removeItem("authToken");
        });
    }
  }, []);

  const login = (token) => {
    localStorage.setItem("authToken", token);
    axios
      .get("http://localhost:5000/api/protected", {
        headers: { "x-auth-token": token },
      })
      .then((response) => {
        setUser(response.data);
      });
  };

  const logout = () => {
    localStorage.removeItem("authToken");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
