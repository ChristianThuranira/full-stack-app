import React from 'react';
import { Card } from 'react-bootstrap';

function LogCard({ log }) {
  return (
    <Card className="mb-3 shadow-lg rounded">
      <Card.Body>
        <Card.Title className="text-center text-warning">{log.completed_date}</Card.Title>
        <div className="d-flex justify-content-between align-items-center">
          <p className="mb-0"><strong>Rating:</strong> {log.rating}/5</p>
          <p className="mb-0"><strong>Notes:</strong> {log.notes}</p>
        </div>
      </Card.Body>
    </Card>
  );
}

export default LogCard;
