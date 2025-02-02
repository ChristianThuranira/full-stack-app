import React, { useEffect, useState } from 'react';
import axios from '../services/api';
import ExerciseCard from '../components/ExerciseCard';

function Exercises() {
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    axios.get('/exercises')
      .then(response => setExercises(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="container mt-5">
      <h2>Exercises</h2>
      {exercises.map(exercise => (
        <ExerciseCard key={exercise.id} exercise={exercise} />
      ))}
    </div>
  );
}

export default Exercises;
