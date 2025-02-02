// /src/components/Dashboard.js

import React from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useHistory } from 'react-router-dom';

const Dashboard = () => {
  const { user, logout } = useAuth();
  const history = useHistory();

  if (!user) {
    history.push('/'); // Redirect to login if user is not logged in
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
