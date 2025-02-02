import React from 'react';
import { Card } from 'react-bootstrap';

function LogCard({ log }) {
  return (
    <Card className="mb-3">
      <Card.Body>
        <Card.Title>Workout Log</Card.Title>
        <p><strong>Completed Date:</strong> {log.completed_date}</p>
        <p><strong>Rating:</strong> {log.rating}/5</p>
        <p><strong>Notes:</strong> {log.notes}</p>
      </Card.Body>
    </Card>
  );
}

export default LogCard;
