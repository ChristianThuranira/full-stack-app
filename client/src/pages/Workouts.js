import React, { useEffect, useState } from 'react';
import axios from '../services/api';
import WorkoutCard from '../components/WorkoutCard';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    axios.get('/workout-plans')
      .then(response => setWorkouts(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleDelete = (id) => {
    axios.delete(`/workout-plans/${id}`)
      .then(() => setWorkouts(workouts.filter(workout => workout.id !== id)))
      .catch(error => console.error(error));
  };

  return (
    <div className="container mt-5">
      <h2>Workout Plans</h2>
      {workouts.map(workout => (
        <WorkoutCard key={workout.id} workout={workout} onDelete={handleDelete} />
      ))}
    </div>
  );
}

export default Workouts;
