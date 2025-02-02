import React from 'react';
import { Card, Button } from 'react-bootstrap';

function WorkoutCard({ workout, onDelete }) {
  return (
    <Card className="mb-3">
      <Card.Body>
        <Card.Title>{workout.title}</Card.Title>
        <Card.Text>{workout.description}</Card.Text>
        <p><strong>Difficulty:</strong> {workout.difficulty_level}</p>
        <p><strong>Time:</strong> {workout.time} minutes</p>
        <p><strong>Calories Burned:</strong> {workout.calories_burned}</p>
        <Button variant="danger" onClick={() => onDelete(workout.id)}>Delete</Button>
      </Card.Body>
    </Card>
  );
}

export default WorkoutCard;
