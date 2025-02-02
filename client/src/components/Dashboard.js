import React, { useContext } from "react";
import { AuthContext } from "../contexts/AuthContext";
import { useHistory } from "react-router-dom";

const Dashboard = () => {
  const { user, logout } = useContext(AuthContext);
  const history = useHistory();

  if (!user) {
    history.push("/login");
    return null;
  }

  return (
    <div>
      <h2>Welcome, {user.username}</h2>
      <button onClick={() => logout()}>Logout</button>
    </div>
  );
};

export default Dashboard;
