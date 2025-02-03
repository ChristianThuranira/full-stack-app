import React from 'react';

function WorkoutCard({ workout, onDelete }) {
  return (
    <div className="workout-card">
      <h3>{workout.title}</h3>
      <p>{workout.description}</p>
      <div className="d-flex justify-content-between">
        <span>{workout.difficulty_level}</span>
        <button onClick={() => onDelete(workout.id)}>Delete</button>
      </div>
    </div>
  );
}

export default WorkoutCard;
