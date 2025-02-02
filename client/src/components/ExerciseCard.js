import React from 'react';
import { Card } from 'react-bootstrap';

function ExerciseCard({ exercise }) {
  return (
    <Card className="mb-3">
      <Card.Body>
        <Card.Title>{exercise.name}</Card.Title>
      </Card.Body>
    </Card>
  );
}

export default ExerciseCard;
