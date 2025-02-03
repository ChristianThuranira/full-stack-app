import React, { useEffect, useState } from 'react';
import axios from '../services/api';
import LogCard from '../components/LogCard';

function Logs() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get('/logs')
      .then(response => setLogs(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="text-center text-warning mb-4">Workout Logs</h2>
      {logs.map(log => (
        <LogCard key={log.id} log={log} />
      ))}
    </div>
  );
}

export default Logs;
