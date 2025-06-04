from datetime import datetime
from notes_app import db

class Note(db.Model):
    """
    Note model representing the structure of our notes table.
    Each note has an ID, title, content, and creation timestamp.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Title cannot be empty
    content = db.Column(db.Text, nullable=False)       # Content cannot be empty
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Automatically set to current time

    def __repr__(self):
        """String representation of the Note object"""
        return f'<Note {self.title}>'

    def to_dict(self):
        """Convert note to dictionary format"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        } 